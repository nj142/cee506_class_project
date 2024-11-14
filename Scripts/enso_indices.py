import pandas as pd
import re
from datetime import datetime, timedelta
import calendar

def ReturnENSOFetch(enso_data_filepath, estimated_breakup_date):
    """
    Fetch ENSO data for 12 months prior to the estimated breakup date (excluding the breakup month)
    
    Args:
        enso_data_filepath (str): Path to the RTF file containing ENSO data
        estimated_breakup_date (datetime): The estimated breakup date
    
    Returns:
        dict: Dictionary with datetime keys and lists of dictionaries containing:
            - month_name (str): Full month name (e.g., "February")
            - month_value (float): ENSO index value
        The list is ordered chronologically from 12 months prior to 1 month prior to breakup
    """
    # Open the file
    with open(enso_data_filepath, 'r', encoding='utf-8') as rtf_file:
        rtf_content = rtf_file.read()
    
    # Parse the data from the RTF file
    data = re.findall(r'(\d+)\s+((?:[-+]?\d*\.\d+|\d+)(?:\s+[-+]?\d*\.\d+|\s+\d+)*)', rtf_content)
    
    # Convert data to a dictionary with years as keys and lists of monthly values
    data_dict = {int(year): list(map(float, months.split())) for year, months in data}
    
    # Create the ENSO index dictionary
    ENSO_index = {}
    
    # Calculate the start date for collecting 12 months of data
    start_date = estimated_breakup_date.replace(day=1) - timedelta(days=1)  # Go to last day of previous month
    start_date = start_date.replace(day=1) - timedelta(days=1)  # Go to last day of month before that
    start_date = start_date.replace(day=1)  # Go to first day of that month
    start_date = start_date - timedelta(days=(11 * 30))  # Go back 11 more months
    
    # Initialize list to store ENSO values with month information
    enso_data = []
    
    # Current date for iteration
    current_date = start_date
    
    # Collect 12 months of data
    while len(enso_data) < 12:
        year = current_date.year
        month = current_date.month
        
        try:
            # Try to get the index value from the parsed data
            monthly_data = data_dict.get(year, [])
            if month <= len(monthly_data):
                value = monthly_data[month - 1]
                month_info = {
                    'month_name': calendar.month_name[month],
                    'month_value': value
                }
                enso_data.append(month_info)
        except (IndexError, TypeError):
            # If no data is available, still include the month info with None value
            month_info = {
                'month_name': calendar.month_name[month],
                'month_value': None
            }
            enso_data.append(month_info)
        
        # Move to next month
        if month == 12:
            current_date = current_date.replace(year=year + 1, month=1)
        else:
            current_date = current_date.replace(month=month + 1)
    
    # Store the values with the end date (month before breakup)
    end_date = estimated_breakup_date.replace(day=1) - timedelta(days=1)
    ENSO_index[end_date] = enso_data
    
    return ENSO_index