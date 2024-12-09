import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import calendar

def return_AO_fetch(ao_data_filepath, breakup_anomaly_data, estimated_breakup_doy):
    """
    Fetch AO data for 12 months prior to the estimated breakup date (excluding the breakup month).
   
    Args:
        ao_data_filepath (str): Path to the AO index data file
        breakup_anomaly_data (dict): Dictionary with years as keys and breakup anomaly data
        estimated_breakup_doy (int): The estimated breakup day of year (DOY)
   
    Returns:
        dict: Dictionary with years as keys and lists of dictionaries containing:
            - month_name (str): Full month name
            - month_value (float): AO index value for that month
    """
    try:
        # Read the data file into a DataFrame
        df = pd.read_csv(ao_data_filepath, delim_whitespace=True, index_col=0)

        # Dictionary to store AO data
        ao_data_dict = {}

        # Iterate over each year in the breakup anomaly data
        for year in breakup_anomaly_data.keys():
            # Determine the breakup month
            breakup_date = datetime(year, 1, 1) + timedelta(days=estimated_breakup_doy - 1)
            breakup_month = breakup_date.month

            # List to store AO data for the 12 months prior to breakup
            ao_month_data = []

            for offset in range(1, 13):  # Iterate over the previous 12 months
                target_month = (breakup_month - offset - 1) % 12 + 1
                target_year = year if breakup_month - offset > 0 else year - 1

                # Fetch the data using month abbreviation
                month_name = calendar.month_name[target_month]
                try:
                    month_value = df.loc[target_year, calendar.month_abbr[target_month]]
                except KeyError:
                    month_value = None  # Handle missing data

                ao_month_data.append({
                    'month_name': month_name,
                    'month_value': month_value
                })

            # Store in the dictionary
            ao_data_dict[year] = ao_month_data

        return ao_data_dict

    except FileNotFoundError:
        print(f"Error: File not found at {ao_data_filepath}")
        return None
    except Exception as e:
        print(f"Error processing AO data: {str(e)}")
        return None
