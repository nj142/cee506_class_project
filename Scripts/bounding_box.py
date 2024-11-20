import pandas as pd
from math import radians, cos, sin, asin, sqrt

def CalculateBoundingBox(data_filepath, site_name, radius_km=100):
    """
    Calculate a bounding box of specified radius around a site's location.
    
    Args:
        data_filepath (str): Path to CSV file containing site coordinates
        site_name (str): Name of the site to create bounding box for
        radius_km (float): Radius of bounding box in kilometers (default 50km)
        
    Returns:
        dict: Dictionary containing min/max lat/lon coordinates
    """
    
    def KmToDeg(km, lat):
        """Convert kilometers to degrees of latitude/longitude."""
        km_per_deg_lat = 111.32
        km_per_deg_lon = abs(cos(radians(lat)) * 111.32)
        deg_lat = km / km_per_deg_lat
        deg_lon = km / km_per_deg_lon
        return deg_lat, deg_lon
    
    try:
        df = pd.read_csv(data_filepath)
        site_data = df[df['site_name'] == site_name].iloc[0]
        lat = site_data['latitude']
        lon = site_data['longitude']
        
        deg_lat, deg_lon = KmToDeg(radius_km, lat)
        
        return {
            'min_lat': lat - deg_lat,
            'max_lat': lat + deg_lat,
            'min_lon': lon - deg_lon,
            'max_lon': lon + deg_lon
        }
            
    except Exception as e:
        raise Exception(f"Error calculating bounding box for {site_name}: {str(e)}")
