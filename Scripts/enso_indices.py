import pandas as pd
import re
from datetime import datetime, timedelta
import calendar

def return_ENSO_fetch(enso_data_filepath, breakup_anomaly_data, estimated_breakup_doy):
    """
    Fetch ENSO data for 12 months prior to the estimated breakup date (excluding the breakup month)
    
    Args:
        enso_data_filepath (str): Path to the RTF file containing ENSO data
        breakup_anomaly_data (dict): Dictionary with years as keys and breakup anomaly data (e.g., zscore, anomaly_days, breakup_date)
        estimated_breakup_doy (int): The estimated breakup day of year (DOY)
    
    Returns:
        dict: Dictionary with years as keys and lists of dictionaries containing:
            - month_name (str): Full month name (e.g., "February")
            - month_value (float): ENSO index value for that month
    """
    # Open the file
    with open(enso_data_filepath, 'r', encoding='utf-8') as rtf_file:
        rtf_content = rtf_file.read()
    
    # Parse the data from the RTF file
    data = re.findall(r'(\d+)\s+((?:[-+]?\d*\.\d+|\d+)(?:\s+[-+]?\d*\.\d+|\s+\d+)*)', rtf_content)
    
    # Convert data to a dictionary with years as keys and lists of monthly values
    data_dict = {int(year): list(map(float, months.split())) for year, months in data}
    
    # Dictionary to store ENSO data for each year
    enso_data_dict = {}
    
    # Iterate over each year in the breakup anomaly data
    for year, breakup_data in breakup_anomaly_data.items():
        # Extract estimated breakup month and year (DOY gives the day of year, need to convert to month)
        breakup_date = datetime(year, 1, 1) + timedelta(days=estimated_breakup_doy - 1)
        breakup_month = breakup_date.month
        
        # List to store ENSO data for the 12 months prior to breakup
        enso_data = []
        
        # Start date is 12 months prior to breakup month (excluding breakup month itself)
        current_date = breakup_date.replace(month=breakup_month - 1 if breakup_month > 1 else 12, day=1)
        
        # Collect 12 months of ENSO data
        for _ in range(12):
            year = current_date.year
            month = current_date.month
            
            # Ensure we don't go out of bounds for the month data
            if year in data_dict and 1 <= month <= len(data_dict[year]):
                month_value = data_dict[year][month - 1]
                enso_data.append({
                    'month_name': calendar.month_name[month],
                    'month_value': month_value
                })
            
            # Move to the previous month
            current_date = current_date.replace(month=month - 1 if month > 1 else 12)
        
        # Store the ENSO data for this year in the dictionary
        enso_data_dict[year] = enso_data
    
    return enso_data_dict
