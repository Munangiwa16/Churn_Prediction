# src/utils.py
"""
Utility functions for Churn Prediction project
"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def selectingK(data, max_k=10):
    """
    Use Elbow Method to find optimal number of clusters for K-means
    
    Parameters:
    -----------
    data : array-like
        Scaled/normalized data for clustering
    max_k : int, default=10
        Maximum number of clusters to test
    
    Returns:
    --------
    None (displays plot)
    
    Plot Output:
    -----------
    Shows elbow curve with K on x-axis and Inertia on y-axis
    
    Example:
    --------
    >>> from sklearn.preprocessing import StandardScaler
    >>> scaler = StandardScaler()
    >>> X_scaled = scaler.fit_transform(X)
    >>> selectingK(X_scaled)
    """
    inertia = []
    K = range(1, max_k)
    
    for k in K:
        km = KMeans(n_clusters=k, random_state=2026, n_init=10)
        km.fit(data)
        inertia.append(km.inertia_)
    
    plt.figure(figsize=(10, 6))
    plt.plot(K, inertia, marker='o', linewidth=2, markersize=8)
    plt.xlabel("Number of clusters (K)", fontsize=12)
    plt.ylabel("Inertia", fontsize=12)
    plt.title("Elbow Method for Optimal K", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def print_model_summary(models_dict, scores_dict):
    """
    Print a summary comparison of model performance
    
    Parameters:
    -----------
    models_dict : dict
        Dictionary with model names as keys and trained models as values
    scores_dict : dict
        Dictionary with model names as keys and test scores as values
    
    Returns:
    --------
    None (prints to console)
    
    Example:
    --------
    >>> models = {'RF': rf_model, 'XGB': xgb_model}
    >>> scores = {'RF': 0.85, 'XGB': 0.88}
    >>> print_model_summary(models, scores)
    """
    print("\n" + "="*60)
    print("MODEL PERFORMANCE SUMMARY")
    print("="*60)
    
    for model_name, score in scores_dict.items():
        print(f"{model_name:.<30} {score:.4f}")
    
    print("="*60)
    print(f"Best Model: {max(scores_dict, key=scores_dict.get)}")
    print(f"Best Score: {max(scores_dict.values()):.4f}")
    print("="*60 + "\n")


def feature_names_after_encoding(original_features, categorical_features):
    """
    Generate feature names after one-hot encoding
    
    Parameters:
    -----------
    original_features : list
        Original feature names
    categorical_features : list
        Names of categorical features to be encoded
    
    Returns:
    --------
    list
        Updated feature names including one-hot encoded features
    
    Note:
    -----
    Actual implementation would need to know unique values in each categorical feature
    """
    numerical_features = [f for f in original_features if f not in categorical_features]
    return numerical_features  # Add encoded feature names as needed
