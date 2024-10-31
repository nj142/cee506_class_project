import pandas as pd
import re
from datetime import datetime

def ReturnENSOFetch(years_of_data, enso_data_filepath):
    # Open the file
    with open(enso_data_filepath, 'r', encoding='utf-8') as rtf_file:
        rtf_content = rtf_file.read()
    
    # Parse the data from the RTF file
    data = re.findall(r'(\d+)\s+((?:[-+]?\d*\.\d+|\d+)(?:\s+[-+]?\d*\.\d+|\s+\d+)*)', rtf_content)
    
    # Convert data to a dictionary with years as keys and lists of monthly values
    data_dict = {int(year): list(map(float, months.split())) for year, months in data}
    
    # Create the ENSO index dictionary
    ENSO_index = {}
    
    for year in years_of_data:
        # Create a list to store ENSO index values for the specific year's context
        ENSO_index_year = []
        
        # Find the relevant months for the year's context (previous year's Oct-Dec and current year's Jan-Mar)
        for y, m in [(year - 1, month) for month in range(10, 13)] + [(year, month) for month in range(1, 4)]:
            try:
                # Try to get the index value from the parsed data
                monthly_data = data_dict.get(y, [])
                if m <= len(monthly_data):
                    value = monthly_data[m - 1]
                    # Create a datetime object for March 1st of the year
                    date_key = datetime(year, 3, 1)
                    ENSO_index_year.append(value)
            except (IndexError, TypeError):
                # Skip if no data is available for the month
                continue
        
        # Store the list of ENSO index values for the year
        if ENSO_index_year:
            ENSO_index[datetime(year, 3, 1)] = ENSO_index_year
    
    return ENSO_index
