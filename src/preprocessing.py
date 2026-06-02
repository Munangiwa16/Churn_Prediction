# src/preprocessing.py
"""
Data preprocessing utilities for Churn Prediction project
"""

import pandas as pd
import numpy as np


def catPreprocessing(dataframe, col_list):
    """
    Apply one-hot encoding to categorical features
    
    Parameters:
    -----------
    dataframe : pandas.DataFrame
        Input dataframe with categorical columns
    col_list : list
        List of column names to encode
    
    Returns:
    --------
    pandas.DataFrame
        Dataframe with categorical features one-hot encoded
    
    Example:
    --------
    >>> X = catPreprocessing(df, ['Contract', 'InternetService'])
    """
    data = dataframe.copy()
    for col in col_list:
        # Create dummies for just this column
        dummies = pd.get_dummies(data[col], prefix=col, dtype=int)
        # Add dummies to dataframe
        data = pd.concat([data, dummies], axis=1)
        # Drop the original column immediately
        data.drop(col, axis=1, inplace=True)
    return data


def targetPrepocessing(target):
    """
    Map target variable to binary numeric values
    
    Parameters:
    -----------
    target : pandas.Series
        Target variable with 'Yes'/'No' values
    
    Returns:
    --------
    pandas.Series
        Mapped target (No=0, Yes=1)
    
    Example:
    --------
    >>> y = targetPrepocessing(df['Churn'])
    """
    target = target.copy()
    target = target.map({"No": 0, "Yes": 1})
    return target


def newDerivedVariables(dataframe):
    """
    Create new derived features from existing ones
    
    Parameters:
    -----------
    dataframe : pandas.DataFrame
        Input dataframe
    
    Returns:
    --------
    pandas.DataFrame
        Dataframe with new derived features
    
    Features Created:
    -----------------
    - AverageCharges: TotalCharges / Tenure
    
    Example:
    --------
    >>> X = newDerivedVariables(df)
    """
    data = dataframe.copy()
    # Average charges per month
    data["AverageCharges"] = data["TotalCharges"] / data["tenure"]
    
    return data
