#  Customer Churn Prediction – End-to-End Data Science Project

This project focuses on predicting customer churn in the telecommunications sector using Machine Learning, and deploying the model as a production-ready API.

---

##  Objective

The goal is to identify customers who are likely to leave a service (churn) in order to help businesses improve retention strategies and reduce customer loss.

---

##  Dataset

- Telecom customer dataset
- Features include:
  - Demographics (gender, senior citizen, etc.)
  - Account information (tenure, contract, payment method)
  - Charges (MonthlyCharges, TotalCharges)
  - Target variable: `Churn`

---

##  Exploratory Data Analysis (EDA)

Key steps performed:

- Handling missing values
- Data type correction
- Correlation analysis
- Feature distribution analysis

###  Key Insights

- Strong correlation between `tenure` and `TotalCharges`
- Moderate correlation between `MonthlyCharges` and `TotalCharges`
- Class imbalance detected in churn distribution
- Data follows a near-normal distribution (validated through histogram)

---

##  Data Preprocessing

- Encoding categorical variables (One-Hot Encoding)
- Standardization of numerical features
- Pipeline creation to avoid data leakage

---

##  Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Random Forest
- XGBoost

###  Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

---

##  Deployment

The model is deployed as an API for real-time predictions.

###  Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
- FastAPI
- Docker

---

##  API Usage

### Endpoint
