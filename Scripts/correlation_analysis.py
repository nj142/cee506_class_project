import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# calculate AO correlation
def calculate_ao_correlation(ao_indices, ice_indices):
    """
    Calculate Pearson correlation between AO indices and ice indices.
    
    Args:
        ao_indices (array-like): AO index values.
        ice_indices (array-like): Ice index values.
    
    Returns:
        dict: Dictionary with correlation coefficient and p-value.
    """
    correlation, p_value = pearsonr(ao_indices, ice_indices)
    return {"correlation": correlation, "p_value": p_value}

# calculate ENSO correlation
def calculate_enso_correlation(enso_indices, ice_indices):
    """
    Calculate Pearson correlation between ENSO indices and ice indices.
    
    Args:
        enso_indices (array-like): ENSO index values.
        ice_indices (array-like): Ice index values.
    
    Returns:
        dict: Dictionary with correlation coefficient and p-value.
    """
    correlation, p_value = pearsonr(enso_indices, ice_indices)
    return {"correlation": correlation, "p_value": p_value}

# plotting the ENSO values
def chart_enso_values(enso_correlation_values, save_path=None):
    """
    Generate a chart for ENSO correlation values.
    
    Args:
        enso_correlation_values (dict): Correlation results for ENSO.
        save_path (str): Path to save the chart. If None, the chart is displayed.
    """
    plt.figure(figsize=(6, 4))
    plt.bar(["ENSO Correlation"], [enso_correlation_values["correlation"]])
    plt.title("ENSO Correlation with Ice Indices")
    plt.ylabel("Correlation Coefficient")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# plotting the AO values 
def chart_ao_values(ao_correlation_values, save_path=None):
    """
    Generate a chart for AO correlation values.
    
    Args:
        ao_correlation_values (dict): Correlation results for AO.
        save_path (str): Path to save the chart. If None, the chart is displayed.
    """
    plt.figure(figsize=(6, 4))
    plt.bar(["AO Correlation"], [ao_correlation_values["correlation"]])
    plt.title("AO Correlation with Ice Indices")
    plt.ylabel("Correlation Coefficient")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
