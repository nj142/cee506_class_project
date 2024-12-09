import pandas as pd
import datetime

def calculate_breakup_data(years_of_data, ice_data_filepath, site_name):
    """
    Calculate breakup data for a specific site across given years.
    
    Parameters:
    years_of_data (list): List of years to process
    ice_data_filepath (str): Path to the ice data CSV file
    site_name (str): Name of the study site
    
    Returns:
    dict: Dictionary of breakup data for each year
    """
    # Read the CSV file
    df = pd.read_csv(ice_data_filepath)
    
    # Filter for the specific site (using Community column)
    site_data = df[df['Community'] == site_name]
    
    # Validate data
    if site_data.empty:
        raise ValueError(f"No data found for site: {site_name}")
    
    # Initialize results dictionary
    breakup_anomaly_data = {}
    
    # Process each year
    for year in years_of_data:
        # Find the data for the current year
        year_data = site_data[site_data['Year'] == year]
        
        if year_data.empty:
            print(f"No data for {site_name} in year {year}")
            continue
        
        # Get the Day of Year (DOY) for breakup
        breakup_doy = year_data['Breakup_DOY'].values[0]
        
        # Convert Day of Year to datetime
        # Assuming breakup occurs in the same year
        breakup_date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=breakup_doy - 1)
        
        # Store data for this year
        breakup_anomaly_data[year] = {
            'breakup_date': breakup_date,
            'zscore_index': year_data['Breakup_Anomaly'].values[0],
            'anomaly_days': year_data['Breakup_Uncertainty'].values[0],
            'breakup_doy': breakup_doy
        }
    
    return breakup_anomaly_data

def calculate_estimated_breakup(breakup_anomaly_data):
    """
    Calculate the estimated breakup date as the mean DOY.

    Parameters:
    breakup_anomaly_data (dict): A dictionary of years with breakup data
    
    Returns:
    float: The estimated breakup date as a DOY
    """
    # If no breakup data is available, return None
    if not breakup_anomaly_data:
        return None

    # Collect all DOYs
    breakup_doys = [data['breakup_doy'] for data in breakup_anomaly_data.values() if data['breakup_doy'] is not None]

    # If no valid DOYs, return None
    if not breakup_doys:
        return None

    # Calculate the mean DOY
    mean_doy = sum(breakup_doys) / len(breakup_doys)

    return mean_doy