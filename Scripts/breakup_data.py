from datetime import datetime
import pandas as pd
import numpy as np
from statistics import mean
from typing import Dict, Any
from datetime import timedelta

def NormalizeValue(value, mean, std):
    """
    Normalize a value using standardization (z-score method).
    
    Parameters:
    value: The value to normalize
    mean: Mean of the baseline period
    std: Standard deviation of the baseline period
    
    Returns:
    float: Normalized value (z-score)
    """
    if std == 0:
        return 0.0
    return (value - mean) / std


from datetime import datetime
from statistics import mean
from typing import Dict, Any

def CalculateEstimatedBreakup(breakup_anomaly_data: Dict[int, Dict[str, Any]]) -> datetime:
    """
    Calculate a single value of estimated breakup date for this site by taking the mean across all years.
    
    Parameters:
    breakup_anomaly_data (dict): Dictionary of integer years (e.g. 2000) with following data subkeys: 
                                zscore_index, anomaly_days, breakup_date
    
    Returns:
    datetime.datetime: datetime object representing the mean breakup date for this site
    
    Raises:
    ValueError: If no valid breakup dates are found in the input data
    TypeError: If breakup_dates are not datetime objects
    """
    # Extract all breakup dates
    breakup_dates = []
    for year_data in breakup_anomaly_data.values():
        if 'breakup_date' not in year_data:
            continue
            
        breakup_date = year_data['breakup_date']
        if not isinstance(breakup_date, datetime):
            raise TypeError(f"Breakup date must be a datetime object, got {type(breakup_date)}")
            
        breakup_dates.append(breakup_date)
    
    if not breakup_dates:
        raise ValueError("No valid breakup dates found in the input data")
    
    # Calculate mean month and day directly
    mean_month = round(mean([date.month for date in breakup_dates]))
    mean_day = round(mean([date.day for date in breakup_dates]))
    
    # Use the first year in the data as reference year
    reference_year = min(breakup_anomaly_data.keys())
    
    return datetime(reference_year, mean_month, mean_day)

def CalculateBreakupData(years_of_data, ice_data_filepath, site_name):
    """
    Calculate normalized ice indices for breakup date anomalies using standardization.
    Each site's z-scores are calculated using only that site's mean and standard deviation.
    
    Parameters:
    years_of_data (list): List of years to analyze
    ice_data_filepath (str): Path to CSV file containing ice data
    site_name (str): Name of the study site to analyze
    
    Returns:
    dict: Dictionary with year keys containing zscore_index, anomaly_days, and breakup_date
    """
    # Read the CSV data
    dataframe = pd.read_csv(ice_data_filepath)
    
    # Filter data for specific site
    site_data = dataframe[dataframe['Community'] == site_name]
    
    if site_data.empty:
        raise ValueError(f"No data found for site: {site_name}")
    
    # Calculate site-specific mean and standard deviation using only this site's data
    site_breakup_mean = site_data['Breakup_Anomaly'].mean()
    site_breakup_std = site_data['Breakup_Anomaly'].std()
    
    # Initialize results dictionary
    results = {}
    
    # Process each year's data for this site
    site_years = site_data[site_data['Year'].isin(years_of_data)]
    
    if site_years.empty:
        raise ValueError(f"No data found for site {site_name} in specified years")
    
    for _, row in site_years.iterrows():
        year = int(row['Year'])
        
        # Normalize breakup anomaly using site-specific standardization
        zscore_index = NormalizeValue(row['Breakup_Anomaly'],
                                     site_breakup_mean, 
                                     site_breakup_std)
        
        # Store values in dictionary
        results[year] = {
            'zscore_index': zscore_index,
            'anomaly_days': row['Breakup_Anomaly'],  # actual days anomaly
            'breakup_date': row['Breakup_Date']  # assuming this column exists in your CSV
        }
    
    return results