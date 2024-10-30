from datetime import datetime
import pandas as pd

def CalculateIceIndex(years_of_data, ice_data_filepath, study_sites):
    # Read the CSV data from the provided filepath
    dataframe = pd.read_csv(ice_data_filepath)
    
    # Initialize an empty dictionary for storing ice anomalies per study site
    ice_anomaly_dict = {site: {} for site in study_sites}
    
    # Loop through each row in the dataframe
    for _, row in dataframe.iterrows():
        year = int(row['Year'])
        community = row['Community']

        # Check if the year is in the provided list of years and the community is a study site
        if year in years_of_data and community in study_sites:
            # Create a datetime object for March 15 of the given year
            anomaly_date = datetime(year=year, month=3, day=15)
            
            # Extract the SLIE_Anomaly (or other index) for this community
            anomaly_value = row['SLIE_Anomaly']
            
            # Add the date and anomaly value to the dictionary for the current site
            ice_anomaly_dict[community][anomaly_date] = anomaly_value

    return ice_anomaly_dict
