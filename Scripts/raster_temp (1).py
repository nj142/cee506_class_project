import xarray as xr
import datetime

def CalculateMean30dTemperature(file_path,bounding_box,estimated_breakup_date):
    start_date = estimated_breakup_date - datetime.timedelta(days=30) #30 days or 31 days in total?
    end_date = estimated_breakup_date

    ds = xr.open_dataset(file_path)
    
    #ds.load()

    temp = ds['TMP_DAILY'] - 273.15#.values
    temp_30d = temp.sel(time=slice(start_date, end_date))
    
    min_lon = bounding_box['min_lon'] + 360
    max_lon = bounding_box['max_lon'] + 360
    
    temp_bbox = temp_30d.sel(
        lat=slice(bounding_box['max_lat'], bounding_box['min_lat']),  #Latitudes go from max to min
        lon=slice(min_lon, max_lon)
    )
    
    mean_30d_temp = temp_bbox.mean().item()
    
    return mean_30d_temp

def CalculateMeanMonthlyTemperature(file_path,bounding_box):
    ds = xr.open_dataset(file_path)
    
    ds.load()
    
    temp = ds['TMP_DAILY']-273.15
    lat = ds['lat']#.values
    lon = ds['lon']#.values
    time = ds['time']#.values
      
    lat_condition = (lat >= bounding_box['min_lat']) & (lat <= bounding_box['max_lat'])
    lon_condition = (lon >= bounding_box['min_lon']+360) & (lon <= bounding_box['max_lon']+360) #Convert lon to 0-360

    extracted_temp = temp.sel(lat=lat[lat_condition], lon=lon[lon_condition])
    
    monthly_temp = extracted_temp.mean(dim=('lat', 'lon'))
    
    return monthly_temp



