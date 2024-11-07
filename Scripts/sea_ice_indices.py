from datetime import datetime
import pandas as pd
import numpy as np

def normalize_value(value, q1, q3, iqr):
    """
    Normalize a value using box plot statistics to a scale from -1 to 1.
    
    Parameters:
    value: The value to normalize
    q1: First quartile
    q3: Third quartile
    iqr: Interquartile range
    
    Returns:
    float: Normalized value between -1 and 1
    """
    if value >= q3 + 1.5 * iqr:
        return 1.0
    elif value <= q1 - 1.5 * iqr:
        return -1.0
    elif value >= q3:
        return 0.5 + 0.5 * (value - q3) / (1.5 * iqr)
    elif value <= q1:
        return -0.5 - 0.5 * (q1 - value) / (1.5 * iqr)
    else:
        return (value - q1) / iqr - 0.5

def CalculateIceIndex(years_of_data, ice_data_filepath, study_sites):
    """
    Calculate normalized ice indices for breakup date anomalies.
    
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
        
        # Calculate quartiles for both metrics
        breakup_stats = site_data['Breakup_Anomaly'].describe()
        
        # Get quartile values for normalization
        breakup_q1 = breakup_stats['25%']
        breakup_q3 = breakup_stats['75%']
        
        # Calculate IQR and bounds
        breakup_iqr = breakup_q3 - breakup_q1
        
        # Process each year's data for this site
        site_years = site_data[site_data['Year'].isin(years_of_data)]
        
        for _, row in site_years.iterrows():
            year = int(row['Year'])
            entry_date = datetime(year=year, month=3, day=1)
            
            # Normalize breakup anomaly
            breakup_norm = normalize_value(row['Breakup_Anomaly'],
                                        breakup_q1, breakup_q3, breakup_iqr)
            
            # Store values in dictionary
            ice_anomaly_dict[site][entry_date] = {
                'breakup_anomaly': {
                    'index': breakup_norm,
                    'actual_days_anomaly': row['Breakup_Anomaly']  # days
                }
            }
    
    return ice_anomaly_dict
