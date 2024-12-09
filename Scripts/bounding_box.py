import pandas as pd
from math import radians, cos, sin, asin, sqrt
from typing import Dict, Union

def calculate_bounding_box(
    data_filepath: str,
    site_name: str,
    radius_km: float = 100
) -> Dict[str, float]:
    def km_to_deg(km: float, lat: float) -> tuple:
        # Constants for conversion
        km_per_deg_lat = 111.32  # kilometers per degree of latitude
       
        # Calculate degrees of latitude
        deg_lat = km / km_per_deg_lat
       
        # Calculate degrees of longitude (depends on latitude)
        km_per_deg_lon = abs(cos(radians(lat)) * 111.32)
        deg_lon = km / km_per_deg_lon
       
        return deg_lat, deg_lon
   
    try:
        # Read the CSV file
        df = pd.read_csv(data_filepath)
       
        # Validate column names
        required_columns = ['Community', 'Latitude', 'Longitude']
        missing_columns = [col for col in required_columns if col not in df.columns]
       
        if missing_columns:
            raise ValueError(f"Missing columns in CSV: {missing_columns}")
       
        # Find the site data
        site_data = df[df['Community'] == site_name]
       
        # Check if site exists
        if site_data.empty:
            # Get list of available sites for user guidance
            available_sites = df['Community'].unique().tolist()
            raise ValueError(
                f"No data found for site: {site_name}. "
                f"Available sites: {available_sites}"
            )
       
        # Extract first matching site's coordinates
        lat = site_data['Latitude'].iloc[0]
        lon = site_data['Longitude'].iloc[0]
       
        # Calculate degrees of latitude and longitude
        deg_lat, deg_lon = km_to_deg(radius_km, lat)
       
        # Return bounding box coordinates
        return {
            'min_lat': lat - deg_lat,
            'max_lat': lat + deg_lat,
            'min_lon': lon - deg_lon,
            'max_lon': lon + deg_lon
        }
   
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {data_filepath}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The CSV file {data_filepath} is empty")
    except Exception as e:
        # Catch-all for any other unexpected errors
        raise ValueError(f"Error calculating bounding box for {site_name}: {str(e)}")