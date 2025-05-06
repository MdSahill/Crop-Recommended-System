# 🌱 Crop Recommendation System - ML to Deployment

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-green)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0-orange)](https://scikit-learn.org/)

**Recommend crops based on soil & weather conditions using ML.**

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [ML Pipeline](#-machine-learning-pipeline)
- [How to Run](#-how-to-run)
- [Demo](#-demo)
- [Contributing](#-contributing)

---

## 🌱 Project Overview
A Flask web app that predicts the best crop using:
- **Input:** Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, rainfall.
- **Output:** Recommended crop + probability scores for all crops.

**Models Used:**  
✔ Random Forest (99.5% accuracy)  
✔ Logistic Regression  
✔ Naive Bayes  

---

## 📊 Dataset
Download from [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset).  
**Columns:** `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall`, `label`.

---

## 🤖 Machine Learning Pipeline
### 1. Preprocessing
**Example:** `Scaling & Encoding`
### 2. Model Training
Train the Random Forest using `ScikitLearn`
### 3. Evaluation
**Model:** `Random Forest`<br>
**Accuracy:** `99.2%`


## 🚀 How to Run
#### Clone the repo:
```python
git clone https://github.com/MdSahill/Crop-Recommendation-System.git
```
#### Install dependencies:
```python
pip install -r requirements.txt
```
#### Run the Flask app:
```python
python app.py
```
#### Open 
http://localhost:5000.

## 🤝 Contributing
### Feel free to:
🔹 Open issues for bugs/feature requests.<br>
🔹 Submit pull requests for improvements.
