# Project Organization Guide

## 📁 Recommended File Structure

```
Churn_Prediction/
├── README.md                          # Project overview (MAIN DOCUMENTATION)
├── REPORT.md                          # Detailed analysis report (MAIN DOCUMENTATION)
├── .gitignore                         # Git ignore file
├── .venv/                             # Virtual environment
│
├── data/                              # All data files
│   ├── train.csv                      # Training dataset (MOVE HERE)
│   ├── test.csv                       # Test dataset (if available)
│   └── data_dictionary.md             # Data description (TO CREATE)
│
├── notebooks/                         # Jupyter notebooks
│   └── Churn_Prediction.ipynb         # Main analysis notebook (MOVE HERE)
│
├── src/                               # Python source code
│   ├── __init__.py
│   ├── preprocessing.py               # Data preprocessing functions
│   ├── feature_engineering.py         # Feature engineering functions
│   ├── model_training.py              # Model training utilities
│   └── utils.py                       # Utility functions
│
├── models/                            # Trained model artifacts
│   ├── random_forest_model.pkl
│   ├── xgboost_model.pkl
│   ├── catboost_model.pkl
│   └── lightgbm_model.pkl
│
├── reports/                           # Analysis outputs and visualizations
│   ├── eda_visualizations/            # EDA plots
│   ├── model_comparison/              # Model performance comparisons
│   └── feature_importance/            # Feature importance plots
│
└── catboost_info/                     # CatBoost training logs (KEEP AS IS)
    ├── catboost_training.json
    ├── learn_error.tsv
    ├── time_left.tsv
    └── learn/
```

## 🎯 File Movement Instructions

### Step 1: Move Data Files
```
Current Location: c:\Users\litho\Documents\Self Learning\Churn_Prediction\train.csv
Move To: c:\Users\litho\Documents\Self Learning\Churn_Prediction\data\train.csv
```
**Why?** Keeps data separate from code and documentation; standard practice for ML projects.

### Step 2: Move Notebook
```
Current Location: c:\Users\litho\Documents\Self Learning\Churn_Prediction\Churn_Prediction.ipynb
Move To: c:\Users\litho\Documents\Self Learning\Churn_Prediction\notebooks\Churn_Prediction.ipynb
```
**Why?** Organizes computational work separately; easier to manage with multiple notebooks.

### Step 3: Move Documentation
```
README.md → Already in root (keep here)
REPORT.md → Already in root (keep here)
```
**Why?** Root-level documentation is immediately visible when opening the project.

### Step 4: Keep Existing Structure
```
.venv/ → Keep in root
catboost_info/ → Keep in root
.idea/ → Keep in root (IDE settings)
```

---

## 📝 Additional Files to Create

### 1. **Data Dictionary** (`data/data_dictionary.md`)
Documents all features, data types, and value ranges.

### 2. **Configuration File** (`config.yaml`)
Stores model parameters, file paths, and hyperparameters.

### 3. **Requirements File** (`requirements.txt`)
Lists all Python dependencies with versions.

### 4. **.gitignore**
Prevents unnecessary files from being committed to version control.

---

## 🚀 Next Steps

1. **Update Notebook Paths**
   - In the notebook, change: `pd.read_csv("train.csv")` 
   - To: `pd.read_csv("./data/train.csv")`

2. **Extract Reusable Code**
   - Move preprocessing functions to `src/preprocessing.py`
   - Move feature engineering to `src/feature_engineering.py`
   - Move model training to `src/model_training.py`

3. **Export Models**
   - Save trained models to `models/` directory with pickle or joblib

4. **Save Visualizations**
   - Export EDA plots to `reports/eda_visualizations/`
   - Export model comparison plots to `reports/model_comparison/`

5. **Create Utility Scripts**
   - `train.py` - Script to train all models
   - `predict.py` - Script for inference on new data
   - `evaluate.py` - Script to evaluate model performance

---

## 📊 Benefits of This Structure

✅ **Scalability**: Easy to add more notebooks, data, or models  
✅ **Reproducibility**: Clear separation of concerns  
✅ **Collaboration**: Others can understand project layout immediately  
✅ **Version Control**: Easier to track changes with Git  
✅ **Best Practices**: Follows ML project conventions  
✅ **Documentation**: Clear documentation at project root  

---

## 📌 Important Notes

- Keep the project root clean - only put README.md, REPORT.md, and config files here
- Always reference data files using relative paths from notebook location
- Update file paths when moving files to new directories
- Use virtual environment (.venv) to manage dependencies
- Add .gitignore to exclude large files and environment folders

---

**Last Updated**: June 2, 2026
