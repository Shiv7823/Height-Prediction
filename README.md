# 🤖 Height Prediction API (FastAPI + Machine Learning)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20Framework-009688?logo=fastapi)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📘 Overview
This project is a **machine learning-powered API** built with **FastAPI** that predicts an individual's height based on parental heights, gender, child order, and number of children using the **Galton Families dataset**.

The API allows users to send input data and receive a **predicted adult height** in real-time.

---

## 🎯 Features
✅ Trained a **Linear Regression Model** using scikit-learn  
✅ Deployed using **FastAPI** for real-time predictions  
✅ Includes **Swagger UI** and **ReDoc** for API documentation  
✅ Modular project structure for easy extension and maintenance  
✅ Clean JSON input-output format  

---

## 🧠 Model Details
- **Algorithm:** Linear Regression  
- **Dataset:** Galton Families Dataset  
- **Accuracy:** ~80%  
- **Input Features:**
  - Father’s height  
  - Mother’s height  
  - Gender  
  - Child order  
  - Number of children  

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/height-prediction-api.git
cd height-prediction-api
