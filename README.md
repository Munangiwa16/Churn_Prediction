# Customer Churn Prediction

## 📋 Project Overview

This project aims to build a machine learning model to predict customer churn for a telecommunications company. The goal is to identify customers who are likely to leave the service so that retention strategies can be implemented proactively.

## 🎯 Objectives

1. **Understand customer churn patterns** through exploratory data analysis
2. **Identify key churn drivers** among customer features
3. **Build and compare multiple machine learning models** for churn prediction
4. **Achieve high predictive accuracy** using ensemble and boosting techniques

## 📊 Dataset

- **File**: `train.csv`
- **Total Records**: Multiple customer records with features and churn status
- **Target Variable**: `Churn` (Yes/No)
- **Missing Values**: No missing values detected
- **Class Imbalance**: ~77.5% No Churn, ~22.5% Churn (Moderate class imbalance)

### Key Features

#### Numerical Features:
- **Tenure**: Customer relationship duration (months)
- **MonthlyCharges**: Customer monthly billing amount
- **TotalCharges**: Total charges for the customer

#### Categorical Features:
- **Demographic**: Gender, SeniorCitizen
- **Account**: Partner, Dependents
- **Services**: PhoneService, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
- **Billing**: Contract, PaperlessBilling, PaymentMethod

## 🔍 Key Findings from EDA

### Numerical Relationships with Churn:

1. **Tenure vs Churn**: Strong inverse relationship
   - Customers with lower tenure are significantly more likely to churn
   - Non-churners have substantially higher median tenure

2. **Total Charges vs Churn**: Positive relationship
   - Churners concentrated at lower total charges
   - Non-churners have wider distribution and higher median

3. **Monthly Charges vs Churn**: Strong positive relationship
   - Higher monthly charges correlate with increased churn
   - Churners concentrated at higher charge levels

4. **Senior Citizen Status**: Moderate relationship
   - Senior citizens have higher churn rate proportionally (despite lower total numbers)

### Categorical Relationships with Churn:

1. **Household Status**: 
   - Customers without partners/dependents show higher churn
   - Stronger household ties may increase retention

2. **Internet Service Type**:
   - Fiber optic: Highest churn rate
   - DSL: Medium churn rate
   - No internet: Lowest churn rate

3. **Value-Added Services** (Strong predictor):
   - Absence of Online Security, Online Backup, Device Protection, Tech Support → Higher churn
   - These services indicate higher customer engagement

4. **Contract Type** (Strongest predictor):
   - Month-to-month contracts: Far higher churn
   - One-year contracts: Much lower churn
   - Two-year contracts: Lowest churn

5. **Payment Method**:
   - Electronic check: Highest churn
   - Other payment methods: Lower churn

6. **Gender**: No significant impact on churn

## 🛠️ Data Preprocessing & Feature Engineering

### Preprocessing Steps:

1. **Categorical Encoding**: One-hot encoding applied to all categorical features
2. **Target Encoding**: Churn mapped to binary (No=0, Yes=1)
3. **Feature Scaling**: StandardScaler applied to numerical features
4. **Train-Test Split**: 75-25 split

### Feature Engineering:

1. **Derived Features**:
   - `AverageCharges`: TotalCharges / Tenure

2. **Clustering Features** (K-means):
   - Applied K-means clustering on scaled numerical features
   - Optimal K=3 determined via Elbow Method
   - Added cluster membership as feature

## 🤖 Models Developed

Four machine learning models were trained and evaluated:

### 1. Random Forest Classifier
- **Parameters Tuned**: n_estimators, max_depth, class_weight, min_samples_split
- **Training Score**: Optimized via RandomizedSearchCV (5-fold CV)
- **Test ROC-AUC Score**: Calculated on test set

### 2. XGBoost Classifier
- **Parameters Tuned**: n_estimators, max_depth, learning_rate, reg_alpha, reg_lambda
- **Strength**: Efficient gradient boosting with regularization
- **Test ROC-AUC Score**: Calculated on test set

### 3. CatBoost Classifier
- **Parameters Tuned**: iterations, max_depth, learning_rate, l2_leaf_reg
- **Strength**: Handles categorical features natively
- **Test ROC-AUC Score**: Calculated on test set

### 4. LightGBM Classifier
- **Parameters Tuned**: n_estimators, learning_rate, num_leaves, lambda_l1, lambda_l2, max_depth
- **Strength**: Fast training with similar boosting benefits
- **Test ROC-AUC Score**: Calculated on test set

## 📈 Model Performance Comparison

| Model | Training ROC-AUC | Test ROC-AUC |
|-------|------------------|-------------|
| Random Forest | 0.9124 | 0.9127 |
| XGBoost | 0.8610 | 0.9166 |
| CatBoost | 0.8610 | 0.9167 |
| LightGBM | 0.8610 | 0.9165 |

*Note: Specific scores are stored in the output of the notebook*

## 💻 Technology Stack

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning preprocessing and models
- **XGBoost**: Gradient boosting framework
- **LightGBM**: Fast gradient boosting
- **CatBoost**: Categorical boosting
- **Matplotlib & Seaborn**: Data visualization

## 📁 Project Structure

```
Churn_Prediction/
├── README.md                    # Project documentation
├── REPORT.md                    # Detailed analysis report
├── data/
│   └── train.csv               # Training dataset
├── notebooks/
│   └── Churn_Prediction.ipynb   # Main analysis notebook
├── models/
│   └── (saved model artifacts)
├── reports/
│   └── (analysis outputs, visualizations)
└── catboost_info/              # CatBoost training logs
    ├── catboost_training.json
    ├── learn_error.tsv
    └── time_left.tsv
```

## 🚀 How to Use

### Prerequisites:
```bash
pip pip install -r requirements.txt
```

### Running the Analysis:
1. Open `Churn_Prediction.ipynb` in Jupyter Notebook or JupyterLab
2. Run cells sequentially from top to bottom
3. Review visualizations and model performance metrics

### Key Sections:
- **Section 0**: Setup and library imports
- **Section 1**: Data loading and exploration
- **Section 2**: Exploratory Data Analysis (EDA)
- **Section 3**: Data preprocessing and feature engineering
- **Section 4**: Model building and evaluation

## 📊 Recommendations

Based on the analysis, the following strategies can help reduce churn:

1. **Focus on Contract Incentives**: Encourage customers to sign longer-term contracts (1-2 years)
2. **Promote Value-Added Services**: Bundle security, backup, and support services
3. **Target High-Risk Segments**: Prioritize retention efforts for:
   - New customers (low tenure)
   - High monthly charge customers
   - Customers using fiber optic internet
   - Customers with month-to-month contracts
4. **Payment Method Optimization**: Encourage alternative payment methods over electronic checks
5. **Senior Citizen Programs**: Develop targeted retention programs for senior customers

## 📝 Next Steps

1. **Model Deployment**: Deploy the best-performing model to production
2. **Model Monitoring**: Implement monitoring for model performance drift
3. **A/B Testing**: Test retention strategies derived from model insights
4. **Feature Updates**: Continuously update and engineer new features
5. **Regular Retraining**: Retrain models with new customer data

## 👤 Author

Created as part of self-learning in machine learning and data science.

