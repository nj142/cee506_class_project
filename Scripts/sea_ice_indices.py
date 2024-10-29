import pandas as pd
from datetime import datetime

def CalculateIceIndex(years_of_data, ice_data_filepath):
    # Read the CSV data from the provided filepath
    dataframe = pd.read_csv(ice_data_filepath)
    
    # Initialize an empty dictionary for storing ice anomalies
    ice_anomaly_dict = {}
    
    # Loop through each row in the dataframe
    for _, row in dataframe.iterrows():
        year = int(row['Year'])
        
        # Check if the year is in the provided list of years
        if year in years_of_data:
            # Create a datetime object for March of the given year
            anomaly_date = datetime(year=year, month=3, day = 15)
            
            # Get the anomaly value
            anomaly_value = row['SLIE_Anomaly']
            
            # Add the date and anomaly value to the dictionary
            ice_anomaly_dict[anomaly_date] = anomaly_value
    
    return ice_anomaly_dict
