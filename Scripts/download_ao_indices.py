import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import calendar

def ReturnAOFetch(file_path, estimated_breakup_date):
    """
    Function that returns Arctic Oscillation (AO) indices for 12 months prior to 
    estimated breakup date (excluding the breakup month).
    
    Parameters:
    -----------
    file_path : str
        Path to the AO index data file
    estimated_breakup_date : datetime
        The estimated breakup date
        
    Returns:
    --------
    dict
        Dictionary with datetime key (first day of month before breakup) and 
        list of dictionaries containing month_name and month_value for the
        12 months prior to breakup month, in chronological order
    
    Notes:
    ------
    Data format expected: Text file with year in first column followed by 12 monthly values
    Data source: https://www.ncei.noaa.gov/access/monitoring/ao/
    """
    try:
        # Read the data file
        with open(file_path, 'r') as f:
            data_lines = f.readlines()
        
        # Process the data into a temporary dictionary with datetime keys
        ao_data = {}
        for line in data_lines[1:]:  # Skip header
            parts = line.strip().split()
            if len(parts) < 13:  # Year + 12 months
                continue
                
            year = int(parts[0])
            ao_values = [float(val) for val in parts[1:]]
            
            # Map each month to its AO value
            for month, ao_value in enumerate(ao_values, start=1):
                date = datetime(year, month, 1)
                ao_data[date] = ao_value
        
        # Initialize the dictionary to store results
        ao_dict = {}
        
        # Calculate the start date for collecting 12 months of data
        start_date = estimated_breakup_date.replace(day=1) - timedelta(days=1)  # Go to last day of previous month
        start_date = start_date.replace(day=1) - timedelta(days=1)  # Go to last day of month before that
        start_date = start_date.replace(day=1)  # Go to first day of that month
        start_date = start_date - timedelta(days=(11 * 30))  # Go back 11 more months
        
        # Initialize list to store AO values with month information
        ao_month_data = []
        
        # Current date for iteration
        current_date = start_date
        
        # Collect 12 months of data
        while len(ao_month_data) < 12:
            try:
                ao_value = ao_data[current_date]
                month_info = {
                    'month_name': calendar.month_name[current_date.month],
                    'month_value': ao_value
                }
            except KeyError:
                # If no data is available for this date
                month_info = {
                    'month_name': calendar.month_name[current_date.month],
                    'month_value': None
                }
                print(f"Warning: Missing data for {current_date.strftime('%B %Y')}")
            
            ao_month_data.append(month_info)
            
            # Move to next month
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)
        
        # Store the values with the end date (month before breakup)
        end_date = estimated_breakup_date.replace(day=1) - timedelta(days=1)
        ao_dict[end_date] = ao_month_data
        
        return ao_dict
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error processing AO data: {str(e)}")
        return None