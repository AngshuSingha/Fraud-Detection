My machine learning capstone project is about spotting fraudulent transactions in mobile money services.I wanted to build something that could catch the bad ones without flagging too many normal ones by mistake. That way financial companies could save money and keep things safer for users. It feels like fraud is a big deal these days with all the digital payments going on.

📊 Dataset Overview

The dataset simulates real-world mobile money transactions and includes features such as:

Transaction amount and type (TRANSFER, CASH_OUT, PAYMENT, etc.)

Sender and receiver account balances (before and after transactions)

Time-based attributes (step/hour, day)

The target variable isFraud indicates whether a transaction is fraudulent.


🛠️ Methodology

Performed data preprocessing and feature engineering to capture transaction behavior

Conducted EDA on the original dataset to understand fraud patterns

Addressed class imbalance using SMOTE

Trained and compared multiple models:

Logistic Regression

Random Forest

XGBoost

Applied Bayesian Optimization for hyperparameter tuning

Evaluated models using Precision, Recall, F1-score, and ROC-AUC


🚀 Key Results

XGBoost emerged as the best-performing model

High recall ensured fewer missed fraud cases

High precision reduced unnecessary customer disruption

Engineered features significantly improved model performance


💡 Business Impact

Reduces financial losses caused by undetected fraud

Lowers investigation costs by minimizing false positives

Demonstrates how ML can support real-time fraud detection systems


📌 Tech Stack

Python | Pandas | NumPy | Scikit-learn | XGBoost | SMOTE | Flask | Power BI
