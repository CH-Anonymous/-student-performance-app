<h1 align="center">📊 Student Performance Analyzer</h1>

<p align="center">
  An interactive <strong>Streamlit AI dashboard</strong> to visualize and predict student performance.<br>
  Built with Python, Pandas, Plotly, Seaborn, and scikit-learn.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/ML-Powered-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Made%20by-Chirag%20Khatri-blueviolet?style=for-the-badge"/>
</p>

---

## ✨ Features

- 📁 Upload student performance CSV files
- 📊 Visualize subject-wise score distributions & correlations
- 📈 Compare scores across gender/class/other categories
- 🤖 Predict student scores using **AI-powered regression**
- 🏅 Highlight top performers with total & average score calculations
- 🎨 Beautiful UI with modern layout, color, and interaction

---

## 🚀 Live Demo

> 🔗 **[Click here to try it online](https://student-performance-predictor-eajqudhgqrwkt9ie5vtvdx.streamlit.app/)**  
> *(or run locally using instructions below)*

---

## 📂 Example CSV Format

```csv
Name, Roll No, Math, Science, Computer, Gender
John Doe, 101, 78, 82, 85, Male
Jane Smith, 102, 92, 88, 91, Female
````

✅ At least two numeric subject columns required
🚫 Avoid IDs being mistaken for scores — e.g., `Roll No`, `Admission No`

---

## 🧑‍💻 Run Locally

### 🔧 Installation

```bash
git clone https://github.com/CH-Anonymous/student-performance-analyzer.git
cd student-performance-analyzer
pip install -r requirements.txt
```

### ▶ Launch App

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🤖 AI Integration

* Built-in **Linear Regression model**
* Predicts any subject based on other subject scores
* Real-time prediction from user input sliders
* No need to train or upload models — it trains on your CSV!

---

## 🛠 Built With

* [Streamlit](https://streamlit.io)
* [Pandas](https://pandas.pydata.org/)
* [scikit-learn](https://scikit-learn.org/)
* [Plotly](https://plotly.com/python/)
* [Seaborn](https://seaborn.pydata.org/)
* [Matplotlib](https://matplotlib.org/)

---

## 📸 Screenshots (Optional)

>
> ### 🔷 Main Dashboard
<p align="center">
  <img src="screenshots/dashboard.png" width="700"/>
</p>

> ### 🔷 AI Score Prediction
<p align="center">
  <img src="screenshots/prediction.png" width="700"/>
</p>

> ### 🔷 Correlation heatmap
<p align="center">
  <img src="screenshots/correlation.png" width="700"/>
</p>

> ### 🔷 Top performer table
<p align="center">
  <img src="screenshots/top_performers.png" width="700"/>
</p>

---

## 📁 Folder Structure

```
📦 student-performance-analyzer/
├── .streamlit/                       
│ └── config.toml
├── screenshots/                         
│   ├── dashboard.png
│   ├── correlation.png
│   ├── top_performers.png
│   └── prediction.png
│  
├── model.pkl                            
├── multi_subject_student_data.csv      
├── app.py                               
├── readme.md                           
├── requirements.txt                     
└── LICENSE                              
```

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it.

---

## 👨‍💻 Author

Made with ❤️ by **Chirag Khatri**
📧 [E-mail](mailto:chiragkhatrigk@gmail.com)
🌐 [Github](https://github.com/CH-Anonymous)

---

> If you like this project, ⭐ star the repo and share it!
