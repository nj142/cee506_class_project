from datetime import datetime
import pandas as pd
import numpy as np

def normalize_value(value, mean, std):
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

def CalculateIceIndex(years_of_data, ice_data_filepath, study_sites):
    """
    Calculate normalized ice indices for breakup date anomalies using standardization.
    
    Parameters:
    years_of_data (list): List of years to analyze
    ice_data_filepath (str): Path to CSV file containing ice data
    study_sites (list): List of study site names to analyze
    
    Returns:
    dict: Nested dictionary with normalized and actual anomaly values for each site and date
    """
    # Read the CSV data
    dataframe = pd.read_csv(ice_data_filepath)
    
    # Initialize the nested dictionary structure
    ice_anomaly_dict = {site: {} for site in study_sites}
    
    # Process each study site separately to calculate site-specific statistics
    for site in study_sites:
        site_data = dataframe[dataframe['Community'] == site]
        
        # Calculate mean and standard deviation for normalization
        breakup_mean = site_data['Breakup_Anomaly'].mean()
        breakup_std = site_data['Breakup_Anomaly'].std()
        
        # Process each year's data for this site
        site_years = site_data[site_data['Year'].isin(years_of_data)]
        
        for _, row in site_years.iterrows():
            year = int(row['Year'])
            entry_date = datetime(year=year, month=3, day=1)
            
            # Normalize breakup anomaly using standardization
            breakup_norm = normalize_value(row['Breakup_Anomaly'],
                                        breakup_mean, breakup_std)
            
            # Store values in dictionary
            ice_anomaly_dict[site][entry_date] = {
                'breakup_anomaly': {
                    'index': breakup_norm,
                    'actual_days_anomaly': row['Breakup_Anomaly']  # days
                }
            }
    
    return ice_anomaly_dict
