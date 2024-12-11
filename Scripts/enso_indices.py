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
    
    date_value_dict = {}

    for year, values in data_dict.items():
        for month, value in enumerate(values, start=1):
            date_value_dict[datetime(year, month, 1)] = value

    # Check the result
    #print(date_value_dict)
    
    # Dictionary to store ENSO data for each year
    enso_data_dict = {}
    
    # Iterate over each year in the breakup anomaly data
    for year in breakup_anomaly_data:
        if year == 2000:
            continue
        
        # Use the estimated breakup DOY
        breakup_doy = estimated_breakup_doy
        
        # Create the breakup date
        breakup_date = datetime(year, 1, 1) + timedelta(days=breakup_doy - 1)
        #breakup_year = breakup_date.year
        breakup_month = breakup_date.month
        
        # List to store ENSO data for the 12 months prior to breakup
        enso_data = []
        
        current_date = breakup_date.replace(year=year - 1)
        year = current_date.year
        month = current_date.month
        
        for _ in range(13):
            
            if year in breakup_anomaly_data and 1 <= month <= 12:
                try:
                    month_value = date_value_dict[datetime(year, month, 1)]
                except KeyError:
                    continue
                enso_data.append({
                    'month_name': calendar.month_name[month],
                    'month_value': month_value
                })
                
            else:
                year += 1
                month = 1
                month_value = date_value_dict[datetime(year, month, 1)]
                enso_data.append({
                    'month_name': calendar.month_name[month],
                    'month_value': month_value
                })
                
            month += 1
        
        # Store the ENSO data for this year in the dictionary
        enso_data_dict[year] = enso_data
    #print(enso_data_dict)
    
    return enso_data_dict