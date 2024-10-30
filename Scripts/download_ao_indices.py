import numpy as np
import pandas as pd
from datetime import datetime

def ReturnAOFetch(years_of_data, file_path):
    """
    Function that returns Arctic Oscillation (AO) indices as a dictionary on monthly scale 
    from March of year-1 to March of current year for each year in years_of_data.
    
    Parameters:
    -----------
    years_of_data : list
        List of years for which to fetch AO indices
    file_path : str
        Path to the AO index data file
        
    Returns:
    --------
    dict
        Dictionary with datetime objects as keys (March 1st of each year) and 
        lists of 13 monthly AO values as values (from March year-1 to March year)
    
    Notes:
    ------
    Data format expected: Text file with year in first column followed by 12 monthly values
    Data source: https://www.ncei.noaa.gov/access/monitoring/ao/
    """
    try:
        # Initialize the dictionary to store results
        ao_dict = {}
        
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
        
        # Extract the required date ranges for each year
        for year in years_of_data:
            start_date = datetime(year-1, 3, 1)
            end_date = datetime(year, 3, 1)
            
            # Check if we have all required dates
            dates_needed = pd.date_range(start=start_date, end=end_date, freq='MS')
            if not all(date in ao_data for date in dates_needed):
                print(f"Warning: Missing data for year {year}")
                continue
            
            # Extract the AO indices for this year's range
            ao_indices = [ao_data[date] for date in dates_needed]
            
            # Store in dictionary using March 1st of the current year as key
            year_datetime = datetime(year, 3, 1)
            ao_dict[year_datetime] = ao_indices
        
        return ao_dict
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error processing AO data: {str(e)}")
        return None

# Example usage:
if __name__ == "__main__":
    # Test the function
    test_years = [2000, 2001, 2005]
    test_file = "monthly.ao.index.txt"
    
    ao_data_dict = ReturnAOFetch(test_years, test_file)
    
    if ao_data_dict:
        for year_date, indices in ao_data_dict.items():
            print(f"\nYear: {year_date.year}")
            print(f"Number of months: {len(indices)}")
            print(f"AO indices: {indices}")