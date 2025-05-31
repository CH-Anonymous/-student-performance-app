import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set Page Configuration
st.set_page_config(page_title="Student Performance Analyzer", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #f7f9fc;
    }
    .block {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    h3 {
        color: #4B8BBE;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='color:#4B8BBE;'>📊 Student Performance Dashboard</h1>", unsafe_allow_html=True)
st.subheader("Analyze subject-wise performance across various demographics.")

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload Student Performance CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower()

     # Step 2: Drop columns with known ID-related keywords
    id_keywords = ['roll', 'sr', 'admission', 'id', 'name', 's.no']
    excluded_cols = [col for col in df.columns if any(key in col for key in id_keywords)]

    # Step 3: Attempt to convert each non-ID column to numeric (for subject scores)
    subject_cols = []
    for col in df.columns:
        if col not in excluded_cols:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                if df[col].notna().sum() > 0:
                    subject_cols.append(col)
            except:
                continue

    # Step 4: All other columns are treated as categorical
    categorical_cols = [col for col in df.columns if col not in subject_cols and col not in excluded_cols]

    # Show warning if no valid subjects
    if not subject_cols:
        st.warning("⚠️ No valid subject columns detected. Please check your CSV file.")
    else:
        # View Data
        with st.expander("🔍 View Uploaded Data"):
            st.dataframe(df)

        # Subject Selector UI Block
        st.markdown("<div class='block'>", unsafe_allow_html=True)
        st.markdown("<h3>🎯 Select Subject to Analyze</h3>", unsafe_allow_html=True)
        subject = st.selectbox("", subject_cols)
        st.markdown("</div>", unsafe_allow_html=True)

        # Correlation Heatmap
        if len(subject_cols) > 1:
            st.markdown("<div class='block'>", unsafe_allow_html=True)
            st.markdown("<h3>📈 Correlation Heatmap</h3>", unsafe_allow_html=True)
            fig, ax = plt.subplots(figsize=(7, 3))
            sns.heatmap(df[subject_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
            st.markdown("</div>", unsafe_allow_html=True)

        # Distribution and Boxplot
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='block'>", unsafe_allow_html=True)
            st.markdown(f"<h3>📊 Distribution of {subject.title()}</h3>", unsafe_allow_html=True)
            fig1 = px.histogram(df, x=subject, nbins=20)
            st.plotly_chart(fig1)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='block'>", unsafe_allow_html=True)
            compare = st.selectbox("📊 Compare with (Boxplot)", ["None"] + subject_cols)
            if compare != "None":
                fig2 = px.box(df, x=compare, y=subject)
                st.plotly_chart(fig2)
            st.markdown("</div>", unsafe_allow_html=True)

        # Regression
        st.markdown("<div class='block'>", unsafe_allow_html=True)
        st.markdown("<h3>📉 Regression Trendline</h3>", unsafe_allow_html=True)
        regress_feature = st.selectbox("Select feature for regression", [col for col in subject_cols if col != subject])
        fig3 = px.scatter(df, x=regress_feature, y=subject, trendline="ols")
        st.plotly_chart(fig3)
        st.markdown("</div>", unsafe_allow_html=True)

        # Overall Score Analysis
        st.markdown("<div class='block'>", unsafe_allow_html=True)
        st.markdown("<h3>🌟 Overall Score Analysis</h3>", unsafe_allow_html=True)
        df["total score"] = df[subject_cols].sum(axis=1)
        df["average score"] = df[subject_cols].mean(axis=1)
        st.dataframe(df[["total score", "average score"] + subject_cols].describe())
        st.markdown("</div>", unsafe_allow_html=True)

        # Top Performers
        st.markdown("<div class='block'>", unsafe_allow_html=True)
        st.markdown("<h3>🏅 Top Performers</h3>", unsafe_allow_html=True)
        top_n = st.slider("Select number of top students to display", 5, 20, 10)
        top_students = df.sort_values(by="total score", ascending=False).head(top_n)
        st.dataframe(top_students[["total score", "average score"] + excluded_cols + subject_cols + categorical_cols])
        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------- 🤖 AI-Powered Score Prediction --------------------

    st.markdown("<div class='block'>", unsafe_allow_html=True)
    st.markdown("<h4>🤖 Predict Student Score with AI</h4>", unsafe_allow_html=True)

    # Select target subject to predict
    target_subject = st.selectbox("🎯 Choose Subject to Predict", subject_cols)

    # Use other subjects as features
    features = [col for col in subject_cols if col != target_subject]

    if len(features) < 1:
        st.warning("❗ Not enough features to train a model.")
    else:
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split

    # Drop rows with missing values
    df_clean = df[features + [target_subject]].dropna()

    X = df_clean[features]
    y = df_clean[target_subject]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    st.markdown("📥 **Enter feature values for prediction:**")
    input_data = []
    for feature in features:
        min_val = float(df[feature].min())
        max_val = float(df[feature].max())
        default_val = float(df[feature].mean())
        val = st.slider(f"{feature.title()}", min_value=min_val, max_value=max_val, value=default_val)
        input_data.append(val)

    # Predict
    if st.button("🔮 Predict Score"):
        predicted = model.predict([input_data])[0]
        st.success(f"✅ Predicted {target_subject.title()} Score: **{predicted:.2f}**")

    st.markdown("</div>", unsafe_allow_html=True)


else:
    st.info("Please upload a CSV file to begin.")
