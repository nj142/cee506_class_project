from netCDF4 import Dataset
import datetime
from datetime import timedelta
import numpy as np
from collections import OrderedDict
import calendar
from scipy import interpolate

def mean_30d_raster_temps(bounding_box, breakup_anomaly_data, estimated_breakup_doy):
    """
    Calculate mean temperature for a 30-day period before breakup for each year in breakup data.
    
    Parameters:
    bounding_box (dict): Dictionary containing min and max latitude and longitude
    breakup_anomaly_data (dict): Dictionary containing breakup anomaly information for different years
    estimated_breakup_doy (int): Estimated Day of Year for breakup
    
    Returns:
    dict: Dictionary of mean temperatures for each year
    """
    # Validate inputs
    if not breakup_anomaly_data:
        raise ValueError("No breakup anomaly data provided")

    # Initialize results dictionary
    temperatures_30day = {}
    
    # Open the dataset using netCDF4
    fp = f'../Data/daily_temps.nc'
    ds = Dataset(fp, 'r')
    
    # Get temperature data (TMP_DAILY), assuming it's stored in Kelvin
    temp = ds.variables['TMP_DAILY'][:]  # All time, lat, lon data as a numpy array
    lat = ds.variables['lat'][:]         # Latitude data
    lon = ds.variables['lon'][:]         # Longitude data
    
    # Convert temperature from Kelvin to Celsius
    temp_celsius = temp - 273.15
    
    # Process each year in the breakup data
    for year in breakup_anomaly_data:
        #print(f"Processing year: {year}")
        # Use the estimated breakup DOY
        breakup_doy = estimated_breakup_doy
        
        # Create the breakup date
        breakup_date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=breakup_doy - 1)
        
        # Define the 30-day period before breakup
        start_date = breakup_date - datetime.timedelta(days=30)
        end_date = breakup_date
        
        # Find the indices for the 30-day period
        time = ds.variables['time'][:]  # Time data
        time_units = ds.variables['time'].units  # Time units, e.g., 'days since 1900-01-01'
        time_origin = datetime.datetime.strptime(time_units.split("since ")[-1], "%Y-%m-%d %H:%M:%S")
        
        # Convert time from days since the origin to datetime
        time_dates = [time_origin + datetime.timedelta(days=t) for t in time]
        
        # Select the indices corresponding to the 30-day period
        start_idx = np.where(np.array(time_dates) >= start_date)[0][0]
        end_idx = np.where(np.array(time_dates) <= end_date)[0][-1]
        
        # Select the temperature data for the 30-day period
        temp_30d = temp_celsius[start_idx:end_idx+1, :, :]
        
        # Convert longitude to 0-360 range
        min_lon = bounding_box['min_lon'] + 360
        max_lon = bounding_box['max_lon'] + 360
        
        # Select latitudes and longitudes within the bounding box
        lat_mask = (lat >= bounding_box['min_lat']) & (lat <= bounding_box['max_lat'])
        lon_mask = (lon >= min_lon) & (lon <= max_lon)
        
        # Extract the subarray for the bounding box
        temp_bbox = temp_30d[:, lat_mask, :][:, :, lon_mask]
        
        # Calculate the mean temperature over lat and lon for the 30-day period
        ave_temperature_30day = np.mean(temp_bbox, axis=0)  # Mean over lat and lon
        temperatures_30day[year] = ave_temperature_30day
    
    # Close the dataset
    ds.close()
    
    return temperatures_30day

def monthly_raster_temps(bounding_box, breakup_anomaly_data, estimated_breakup_doy):
    fp = f'../Data/monthly_temps.nc'
    ds = Dataset(fp, 'r')
    
    temp = ds.variables['TMP_DAILY'][:]
    lat = ds.variables['lat'][:]
    lon = ds.variables['lon'][:]     
    time = ds['time'][:]
    
    temp_celsius = temp - 273.15
    
    # Extract latitude and longitude indices based on bounding box
    lat_condition = (lat >= bounding_box['min_lat']) & (lat <= bounding_box['max_lat'])
    lon_condition = (lon >= bounding_box['min_lon'] + 360) & (lon <= bounding_box['max_lon'] + 360)  # Convert lon to 0-360
    
    lat_indices = np.where(lat_condition)[0]
    lon_indices = np.where(lon_condition)[0]
    
    # Extract the temperature data for the bounding box
    temp_bbox = temp_celsius[:, lat_indices, :][:, :, lon_indices]
    
    # Get the start date and convert time
    start_date = datetime.datetime(2000, 1, 31)
    dates = [start_date + datetime.timedelta(days=int(day)) for day in time]
    year_month_day = [(date.year, date.month, date.day) for date in dates]
    
    # Create a dictionary with dates as keys
    date_temp_dict = {date: temp for date, temp in zip(dates, temp_bbox)}
    
    # Make all days as the first of each month
    new_date_temp_dict = OrderedDict()
    for date, temp_data in date_temp_dict.items():
        new_date = date.replace(day=1)
        new_date_temp_dict[new_date] = temp_data
    
    monthly_temp_dict = {}
    
    # Now iterate over the breakup anomaly data for each year
    for year in breakup_anomaly_data:   
        if year == 2000:
            continue
        
        # Use the estimated breakup DOY
        breakup_doy = estimated_breakup_doy
        
        # Create the breakup date
        breakup_date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=breakup_doy - 1)
        breakup_month = breakup_date.month
        monthly_temp_data = []
        
        current_date = breakup_date.replace(year=year - 1)
        year = current_date.year
        month = current_date.month
        
        for _ in range(13):
            if year in breakup_anomaly_data and 1 <= month <= 12:
                try:
                    month_value = new_date_temp_dict[datetime.datetime(year, month, 1)]
                except KeyError:
                    continue
                monthly_temp_data.append({
                    'month_name': calendar.month_name[month],
                    'month_value': month_value
                })
            else:
                year += 1
                month = 1
                month_value = new_date_temp_dict[datetime.datetime(year, month, 1)]
                monthly_temp_data.append({
                    'month_name': calendar.month_name[month],
                    'month_value': month_value
                })
            
            month += 1
        
        # Store the temperature data for the current year
        monthly_temp_dict[year] = monthly_temp_data

    return monthly_temp_dict

    """
    Calculate monthly temperature for a given bounding box.
    
    Parameters:
    bounding_box (dict): Dictionary containing min and max latitude and longitude
    
    Returns:
    xarray.DataArray: Monthly temperature data
    """