import cdsapi
import xarray as xr
import numpy as np

def mean_30d_raster_temps(bounding_box,estimated_breakup_date):

    year = estimated_breakup_date.year
    start_date = estimated_breakup_date - datetime.timedelta(days=30)
    start_month = start_date.month
    start_day = start_date.day
    end_month = estimated_breakup_date.month
    end_day = estimated_breakup_date.day

    dataset = "reanalysis-era5-pressure-levels"
    request = {
        "product_type": ["reanalysis"],
        "variable": ["2m_temperature"],
        "year": year,
        "month": [f"{start_month:02d}", f"{end_month:02d}"] if start_month != end_month else [f"{end_month:02d}"],
        "day": [f"{d:02d}" for d in range(start_day, 32)] if start_month != end_month else [f"{d:02d}" for d in range(start_day, end_day + 1)],
        "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
        ],
        "pressure_level": ["1000"],
        "data_format": "netcdf",
        "download_format": "unarchived",
        "area": [bounding_box['max_lat'], bounding_box['min_lon'], bounding_box['min_lat'], bounding_box['max_lon']]
    }

    client = cdsapi.Client()
    client.retrieve(dataset, request).download("mean_30d_raster_temps.nc")

    ds = xr.open_dataset("mean_30d_raster_temps.nc")
    time = ds.variables['valid_time']
    lat = ds.variables['latitude']
    lon = ds.variables['longitude']
    t2m = ds.variables['t2m']

    mean_30d_temps = np.mean(t2m)

    return mean_30d_temps

mean_30d_raster_temps(bounding_box,estimated_breakup_date)

def monthly_raster_temps(bounding_box):

    dataset = "reanalysis-era5-land-monthly-means"
    request = {
        "product_type": ["monthly_averaged_reanalysis"],
        "variable": ["2m_temperature"],
        "year": [
            "2000", "2001", "2002",
            "2003", "2004", "2005",
            "2006", "2007", "2008",
            "2009", "2010", "2011",
            "2012", "2013", "2014",
            "2015", "2016", "2017",
            "2018", "2019", "2020",
            "2021", "2022"
        ],
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
        ],
        "time": ["00:00"],
        "data_format": "netcdf",
        "download_format": "unarchived",
        "area": [bounding_box['max_lat'], bounding_box['min_lon'], bounding_box['min_lat'], bounding_box['max_lon']]
    }

    client = cdsapi.Client()
    client.retrieve(dataset, request).download("")
    
    ds = xr.open_dataset("")
    time = ds.variables['valid_time']
    lat = ds.variables['latitude']
    lon = ds.variables['longitude']
    t2m = ds.variables['t2m']

    return t2m

monthly_raster_temps(bounding_box)



