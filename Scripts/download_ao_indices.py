import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime, date
import pandas as pd
import matplotlib.dates as mdates
import os
#df_ao = pd.read_csv(r"monthly.ao.txt", sep="\s+") 

def ReturnAOFetch(years_of_data, file_path):
    """
    Function that returns AO indices as a dictionary on monthly scale from March of start_year-1 to March end_year
    """
    # read text file into pandas DataFrame
    # data retrieved from: https://www.ncei.noaa.gov/access/monitoring/ao/   
    #data_file = os.path.join('..', 'Data', 'monthly.ao.index.txt')
    ao_dict = {}

    with open(file_path, 'r') as f:
        data_lines = f.readlines()

    ao_data = {}
    for line in data_lines[1:]: # skipping header
        #yyyy/mm/dd
        parts = line.strip().split()
        year = int(parts[0])
        ao_values = list(map(float, parts[1:]))

        # map each month in current year to AO value
        for month, ao_value in enumerate(ao_values, start=1):
            date = datetime(year, month, 1)
            ao_data[date] = ao_value
            #print(f"Added {date} : {ao_value} to ao_data")


    for year in years_of_data:
        start_date = datetime(year-1, 3, 1) 
        end_date = datetime(year, 3, 1)
        #print(f"\nExtracting data for year {year} from {start_date} to {end_date}")
        ao_indices = [ao_data[date] for date in ao_data if start_date <= date <= end_date]
        #print(f"Extracted AO indices for {year}: {ao_indices}")  

        year_datetime = datetime(year, 3, 1)
        # store in dictionary
        ao_dict[year_datetime] = ao_indices

    return ao_dict

"""
This code can be executed to test the function locally. The only changes that needs to be made to the main code:
- Add file_path as an input to the function
- Comment out data_file 
- Change filepath below to your own

# test locally on desktop
file_path = r"C:\Users\Valerie Tsao\Documents\PhD\CEE506 - ESDA\monthly.ao.index.txt"   # needs to be changed 
years=[2000, 2001, 2005]
ao_data_dict = ReturnAOFetch(file_path, years)
print(ao_data_dict)
"""