# 📏 Height Prediction System (Machine Learning + Streamlit)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📘 Overview
This project is a **Machine Learning–based web application** that predicts a child’s **estimated adult height** using parental and demographic data.

The application is built using **Streamlit** for an interactive user interface and **scikit-learn** for model training and prediction.  
It provides both a predicted height and an **expected confidence range**, making the prediction more realistic and transparent.

⚠️ *Height prediction is an estimation problem and results may vary due to biological and environmental factors.*

---

## 🎯 Features
- Interactive **Streamlit web interface**
- Machine Learning model trained on real-world data
- Feature engineering using **mid-parent height**
- Displays **confidence range (± error margin)**
- Visual comparison of parent heights and predicted height
- Clear explanation of model behavior and limitations
- Suitable for **academic projects, demos, and portfolios**

---

## 🧠 Model Details
- **Algorithm:** Random Forest Regressor  
- **Dataset Size:** 936 records  
- **Target Variable:** Height (cm)  

### Feature Engineering
- Mid-parent height = (Father Height + Mother Height) / 2  

### Input Features
- Father’s height (cm)
- Mother’s height (cm)
- Total number of children
- Child birth order
- Gender

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

> The model predicts an **estimated height with an acceptable error margin**, not an exact value.

---

## 📊 Application Interface
The web application includes:
- User-friendly input form with explanations
- Predicted height output
- Expected height range (confidence interval)
- Bar chart comparing parent heights and predicted height
- Model transparency and limitations section

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/height-prediction-system.git
cd height-prediction-system
