# src/__init__.py
"""
Churn Prediction Project - Utility Modules
"""

__version__ = "1.0.0"
__author__ = "Data Science Team"

from .preprocessing import (
    catPreprocessing,
    targetPrepocessing,
    newDerivedVariables,
)
from .utils import (
    selectingK,
)

__all__ = [
    'catPreprocessing',
    'targetPrepocessing',
    'newDerivedVariables',
    'selectingK',
]
