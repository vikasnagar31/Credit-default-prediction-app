# 🏦 Credit Default Prediction App

A machine learning-powered web application to predict whether a bank customer is likely to **default on a loan**. This project uses **Random Forest** and **Logistic Regression (statsmodels)** to model the **Probability of Default (PD)** and provides both statistical and ML-based credit risk analytics.

Deployed using **Flask** with a web interface for real-time customer default prediction.

---

## 📊 Project Motivation

In banking, predicting the likelihood of a customer defaulting on a loan is crucial for risk management. This project aims to build an accurate credit risk model using historical loan data and deploy it as an interactive web app to assist decision-makers in real time.

---

## 📁 Dataset Overview

The dataset used is `bankloans.csv`, which contains customer demographic and financial attributes.  
Each row represents a customer with the following features:

### 🔍 Feature Description:

| Feature     | Description                                   |
|-------------|-----------------------------------------------|
| `age`       | Age of the customer (in years)                |
| `ed`        | Education level (categorical: 1–5)            |
| `employ`    | Years of employment                           |
| `address`   | Years at current address                      |
| `income`    | Annual income in thousands                    |
| `debtinc`   | Debt-to-Income ratio                          |
| `creddebt`  | Amount of credit card debt                    |
| `othdebt`   | Other debt obligations                        |
| `default`   | Target variable (1 = default, 0 = no default) |

---

## 🧠 Models Used

### 1. **Random Forest Classifier (ML Approach)**
- Feature Selection: Recursive Feature Elimination (RFE)
- Hyperparameter Tuning: GridSearchCV
- Evaluation: Confusion Matrix, Accuracy, ROC-AUC

### 2. **Logistic Regression (Statistical Approach)**
- Using `statsmodels`
- P-value-based feature selection
- Interpretable coefficients for business insights

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Jupyter Notebook** (for EDA, modeling)
- **Flask** (for web app)
- **HTML/CSS** (for frontend UI)
- **Git & GitHub** (for version control)
- **Render / Heroku** (for deployment)

---

## 🚀 How to Use

### 🔧 Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/vikasnagar31/Credit-default-prediction-app.git
   cd Credit-default-prediction-app
