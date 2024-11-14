import pandas as pd
from math import radians, cos, sin, asin, sqrt

class CalculateBoundingBox:
    def __init__(self, data_filepath, site_name, radius_km=50):
        """
        Calculate a bounding box of specified radius around a site's location.
        
        Args:
            data_filepath (str): Path to CSV file containing site coordinates
            site_name (str): Name of the site to create bounding box for
            radius_km (float): Radius of bounding box in kilometers (default 50km)
        """
        self.data_filepath = data_filepath
        self.site_name = site_name
        self.radius_km = radius_km
        self.bbox = self._calculate_bbox()
    
    def _km_to_deg(self, km, lat):
        """Convert kilometers to degrees of latitude/longitude."""
        # Earth's radius in km
        earth_radius = 6371.0
        
        # 1 degree of latitude is approximately 111.32 km
        km_per_deg_lat = 111.32
        
        # 1 degree of longitude varies with latitude
        km_per_deg_lon = abs(cos(radians(lat)) * 111.32)
        
        # Convert distance to degrees
        deg_lat = km / km_per_deg_lat
        deg_lon = km / km_per_deg_lon
        
        return deg_lat, deg_lon
    
    def _calculate_bbox(self):
        """
        Calculate the bounding box coordinates.
        
        Returns:
            dict: Dictionary containing min/max lat/lon coordinates
        """
        try:
            # Read the data file
            df = pd.read_csv(self.data_filepath)
            
            # Get the site's coordinates
            site_data = df[df['site_name'] == self.site_name].iloc[0]
            lat = site_data['latitude']
            lon = site_data['longitude']
            
            # Calculate degree offsets for the bounding box
            deg_lat, deg_lon = self._km_to_deg(self.radius_km, lat)
            
            # Calculate bounding box coordinates
            bbox = {
                'min_lat': lat - deg_lat,
                'max_lat': lat + deg_lat,
                'min_lon': lon - deg_lon,
                'max_lon': lon + deg_lon
            }
            
            return bbox
            
        except Exception as e:
            raise Exception(f"Error calculating bounding box for {self.site_name}: {str(e)}")
    
    def get_bbox(self):
        """Return the calculated bounding box coordinates."""
        return self.bbox
    
    def contains_point(self, lat, lon):
        """
        Check if a point falls within the bounding box.
        
        Args:
            lat (float): Latitude of point to check
            lon (float): Longitude of point to check
            
        Returns:
            bool: True if point is within bounding box, False otherwise
        """
        return (self.bbox['min_lat'] <= lat <= self.bbox['max_lat'] and
                self.bbox['min_lon'] <= lon <= self.bbox['max_lon'])

# Example usage:
# bbox_calculator = CalculateBoundingBox('site_coordinates.csv', 'Utqiagvik')
# bbox = bbox_calculator.get_bbox()
# print(f"Bounding box coordinates: {bbox}")