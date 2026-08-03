# 🏦 SmartLoan AI

A Machine Learning-powered Loan Approval Prediction System built using **Flask**, **Scikit-Learn**, **Docker**, and **Bootstrap**.

The application predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant information such as income, CIBIL score, assets, and loan details.

---

## 🚀 Live Demo

**Live Application:** https://your-render-url.onrender.com

---

## 📸 Screenshots

### Home Page

Add Screenshot Here

### Prediction Result

Add Screenshot Here

---

## ✨ Features

- Machine Learning based loan approval prediction
- Beautiful responsive Bootstrap UI
- Confidence score for each prediction
- REST API support
- Dockerized application
- Ready for cloud deployment (Render)
- Clean project structure
- Fast prediction using a trained Random Forest model

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-Learn
- Random Forest Classifier
- NumPy
- Pandas
- Joblib
- Bootstrap 5
- Docker
- Render

---

## 📂 Project Structure

```
loan_approval_project/
│
├── app.py
├── predictor.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── models/
│   └── loan_approval_pipeline.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── dataset/
│
└── notebooks/
```

---

## 📊 Input Features

The model uses the following applicant information:

- Number of Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Asset Value
- Commercial Asset Value
- Luxury Asset Value
- Bank Asset Value

---

## 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Pipeline Includes:

- StandardScaler
- Random Forest Classifier

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Roshan-shetty20/loan_approval_project.git
```

Go to project folder

```bash
cd loan_approval_project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://localhost:5000
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t smartloan-ai .
```

Run Docker Container

```bash
docker run -d -p 5000:5000 smartloan-ai
```

Application URL

```
http://localhost:5000
```

---

## 🔌 REST API

### Endpoint

```
POST /api/predict
```

### Sample Request

```json
{
    "no_of_dependents": 2,
    "education": 1,
    "self_employed": 0,
    "income_annum": 500000,
    "loan_amount": 100000,
    "loan_term": 10,
    "cibil_score": 750,
    "residential_assets_value": 3000000,
    "commercial_assets_value": 0,
    "luxury_assets_value": 500000,
    "bank_asset_value": 400000
}
```

### Sample Response

```json
{
    "prediction": "Loan Approved",
    "confidence": 96.42
}
```

---

## 🎯 Future Improvements

- User Authentication
- Explainable AI (SHAP)
- Prediction History
- Database Integration
- Admin Dashboard
- Model Retraining Pipeline
- CI/CD using GitHub Actions
- AWS Deployment

---

## 👨‍💻 Author

**Roshan Shetty**

GitHub

https://github.com/Roshan-shetty20
# 🏦 SmartLoan AI

A Machine Learning-powered Loan Approval Prediction System built using **Flask**, **Scikit-Learn**, **Docker**, and **Bootstrap**.

The application predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant information such as income, CIBIL score, assets, and loan details.

---

## 🚀 Live Demo

**Live Application:** https://your-render-url.onrender.com

---

## 📸 Screenshots

### Home Page

Add Screenshot Here

### Prediction Result

Add Screenshot Here

---

## ✨ Features

- Machine Learning based loan approval prediction
- Beautiful responsive Bootstrap UI
- Confidence score for each prediction
- REST API support
- Dockerized application
- Ready for cloud deployment (Render)
- Clean project structure
- Fast prediction using a trained Random Forest model

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-Learn
- Random Forest Classifier
- NumPy
- Pandas
- Joblib
- Bootstrap 5
- Docker
- Render

---

## 📂 Project Structure

```
loan_approval_project/
│
├── app.py
├── predictor.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── models/
│   └── loan_approval_pipeline.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── dataset/
│
└── notebooks/
```

---

## 📊 Input Features

The model uses the following applicant information:

- Number of Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Asset Value
- Commercial Asset Value
- Luxury Asset Value
- Bank Asset Value

---

## 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Pipeline Includes:

- StandardScaler
- Random Forest Classifier

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Roshan-shetty20/loan_approval_project.git
```

Go to project folder

```bash
cd loan_approval_project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://localhost:5000
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t smartloan-ai .
```

Run Docker Container

```bash
docker run -d -p 5000:5000 smartloan-ai
```

Application URL

```
http://localhost:5000
```

---

## 🔌 REST API

### Endpoint

```
POST /api/predict
```

### Sample Request

```json
{
    "no_of_dependents": 2,
    "education": 1,
    "self_employed": 0,
    "income_annum": 500000,
    "loan_amount": 100000,
    "loan_term": 10,
    "cibil_score": 750,
    "residential_assets_value": 3000000,
    "commercial_assets_value": 0,
    "luxury_assets_value": 500000,
    "bank_asset_value": 400000
}
```

### Sample Response

```json
{
    "prediction": "Loan Approved",
    "confidence": 96.42
}
```

---

## 🎯 Future Improvements

- User Authentication
- Explainable AI (SHAP)
- Prediction History
- Database Integration
- Admin Dashboard
- Model Retraining Pipeline
- CI/CD using GitHub Actions
- AWS Deployment

---

## 👨‍💻 Author

**Roshan Shetty**

GitHub

https://github.com/Roshan-shetty20

LinkedIn
https://www.linkedin.com/in/roshan-shetty05

[text](.git) [text](__pycache__) [text](dataset) [text](models) [text](notebook) [text](screenshot) [text](static) [text](templates) [text](.gitignore) [text](app.py) [text](config.py) [text](Dockerfile) [text](gradio_app.py) [text](predictor.py) [text](README.md) [text](requirements.txt)
---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
