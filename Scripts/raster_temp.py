import xarray as xr
import datetime

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
    mean_temperatures = {}
    
    # Open the dataset once to improve performance
    fp = '../Data/daily_temps.nc'
    ds = xr.open_dataset(fp)
    
    # Convert temperature to Celsius
    temp = ds['TMP_DAILY'] - 273.15
    
    # Process each year in the breakup data
    for year, breakup_info in breakup_anomaly_data.items():
        # Use the estimated breakup DOY
        breakup_doy = estimated_breakup_doy
        
        # Create the breakup date
        breakup_date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=breakup_doy - 1)
        
        # Define 30-day period before breakup
        start_date = breakup_date - datetime.timedelta(days=30)
        end_date = breakup_date
        
        # Select temperature data for the 30-day period
        temp_30d = temp.sel(time=slice(start_date, end_date))
        
        # Convert longitude to 0-360 range
        min_lon = bounding_box['min_lon'] + 360
        max_lon = bounding_box['max_lon'] + 360
        
        # Select temperature data within the bounding box
        temp_bbox = temp_30d.sel(
            lat=slice(bounding_box['max_lat'], bounding_box['min_lat']),  # Latitudes go from max to min
            lon=slice(min_lon, max_lon)
        )
        
        # Calculate mean temperature
        try:
            mean_30d_temp = temp_bbox.mean().item()
            mean_temperatures[year] = {
                'mean_temp': mean_30d_temp,
                'breakup_doy': breakup_doy,
                'breakup_date': breakup_date
            }
        except Exception as e:
            print(f"Could not calculate mean temperature for {year}: {e}")
    
    # Close the dataset
    ds.close()
    
    return mean_temperatures

def calculate_monthly_temperature(bounding_box):
    """
    Calculate monthly temperature for a given bounding box.
    
    Parameters:
    bounding_box (dict): Dictionary containing min and max latitude and longitude
    
    Returns:
    xarray.DataArray: Monthly temperature data
    """
    fp = '../Data/monthly_temps.nc'
    ds = xr.open_dataset(fp)
    
    ds.load()
    
    # Convert temperature to Celsius
    temp = ds['TMP_DAILY'] - 273.15
    lat = ds['lat']
    lon = ds['lon']
    
    # Create conditions for latitude and longitude
    lat_condition = (lat >= bounding_box['min_lat']) & (lat <= bounding_box['max_lat'])
    lon_condition = (lon >= bounding_box['min_lon']+360) & (lon <= bounding_box['max_lon']+360)  # Convert lon to 0-360
    
    # Extract temperature data within the bounding box
    extracted_temp = temp.sel(lat=lat[lat_condition], lon=lon[lon_condition])
    
    # Calculate monthly mean temperature
    monthly_temp = extracted_temp.mean(dim=('lat', 'lon'))
    
    return monthly_temp