"""
Transformer Class for implement the transformation process 

Author: Giuseppe Valente <valentepeppe@gmail.com>

Usage:
    - Create an instance of Transformer.
    - Call methods transform(raw_data) passing the raw_data from Executioner
"""

from models.meteorite_landing_raw import MeteoriteLandingRaw
from models.dimension_date_model import DimensionDateModel
from models.meteorite_model import MeteoriteModel
from models.dimension_location_model import DimensionLocationModel
from models.dimension_classification_model import DimensionClassificationModel
from models.meteorite_type import MeteoriteType
from typing import List

import sys
import geopandas as gpd
from shapely.geometry import Point
from math import isclose
from models.meteorite_type import MeteoriteType

import time



class Transformer:

    """
    A class to transform raw meteorite landing data into structured `MeteoriteModel` instances.

    Attributes:
        raw_data (list): A list of raw meteorite landing from the Extractor
        transformed_data (List[MeteoriteModel]): A list to store the transformed `MeteoriteModel` instances.
        location_cache (dict): A cache to store the transformed location data to avoid redundant API calls.
    """    


    def __init__(self, raw_data):
        """
        Initializes the Transformer with raw meteorite landing data.

        Args:
            raw_data (list): A list containing raw meteorite landing data.
        """
        self.raw_data = raw_data
        self.transformed_data: List[MeteoriteModel] = []
        self.location_cache = {} # Cache a simple hash map of location

    def transform(self):

        """
        Transforms the raw data into `MeteoriteModel` instances and stores them in `transformed_data`.

        The method processes each item in `raw_data`, cleans it, transforms location data, and creates `MeteoriteModel`
        instances.
        """
        
        progress = 0
        for item in self.raw_data:

            percentage = (progress/len(self.raw_data)) * 100
            sys.stdout.write(f"\rProgress: {percentage:.2f}%")
            sys.stdout.flush()

            tmp = self.__clean(item)
            if(tmp is None):
                progress = progress + 1
                continue

            date = DimensionDateModel(tmp.year)
            if(date is None):
                progress = progress + 1
                continue

            
            primitive_achonrdites = MeteoriteType.primitive_achonrdites(tmp.recclass)
            achonrdites = MeteoriteType.achonrdites(tmp.recclass)
            chondrites = MeteoriteType.chondrites(tmp.recclass)

            # Determine classification
            classification = (primitive_achonrdites or achonrdites or chondrites)
            
            # Check if classification was found
            if classification is None:
                progress += 1
                continue
        
            location = None
            while True:
                try:
                    location = self.__transform_location_dimension((tmp.reclat, tmp.reclong))
                    break # exit from while
                except Exception as e:
                    print(f" Location ({tmp.reclat}, {tmp.reclong}) fails, we need to wait the API limit - 1 second waiting before to send a new request")
                    time.sleep(1) # 1 second
                
            if(location is None):
                progress = progress + 1
                continue
                
            m = MeteoriteModel(
                dimensionDateModel = date,
                mass = tmp.mass,
                dimensionLocationModel=location,
                dimensionClassificationModel=classification
            )

            self.transformed_data.append(m)
            progress = progress + 1
        

    def __clean(self, item) -> MeteoriteLandingRaw:

        """
        Cleans and validates raw meteorite landing data.

        Args:
            item: The raw meteorite landing data.

        Returns:
            MeteoriteLandingRaw: A cleaned and validated `MeteoriteLandingRaw` instance, or None if the data is invalid.
        """

        recclass = item.get('recclass')
        if(recclass is None or len(recclass) == 0):
            return None
        
        mass = item.get('mass')
        if(mass is None or len(mass) == 0 or float(mass) == 0):
            return None
        
        date = item.get('year')
        if(date is None or len(date) == 0):
            return None
        
        lat = item.get('reclat')
        if(lat is None or len(lat) == 0):
            return None
        
        long = item.get('reclong')
        if(long is None or len(long) == 0):
            return None
        
        # Remove not reversable locations
        if(not self.__recoverable_location(lat=float(lat), lon=float(long))):
            return None

        return MeteoriteLandingRaw(
            recclass = recclass,
            mass = float(mass),
            year = date,
            reclat = round(float(lat), 1),
            reclong = round(float(long), 1)
        )

    def __transform_location_dimension(self, position:tuple):

        """
        Transforms coordinates into a `DimensionLocationModel` instance using reverse geocoding.

        Args:
            position (tuple): A tuple containing latitude and longitude.

        Returns:
            DimensionLocationModel: A `DimensionLocationModel` instance with location details, or None if the location couldn't be resolved.
        """

        coordinates = (round(position[0], 1), round(position[1], 1))
        
        if coordinates in self.location_cache:
            return self.location_cache[coordinates] # Value present in cache
        
        point = Point(coordinates[1], coordinates[0])
        time.sleep(0.3)
        loc = gpd.tools.reverse_geocode(point)
        address = loc["address"][0]
        tmp = None
        if(address is not None and len(address) > 0):
            tmp = DimensionLocationModel(latitude=coordinates[0], longitude=coordinates[1], state=None, country=None, city=None)
            split_string = [s.strip() for s in address.split(',')]
            tmp.city = split_string[len(split_string) - 3] or None
            tmp.state = split_string[len(split_string) - 2] or None
            tmp.country = split_string[len(split_string) - 1] or None
        
        # Add item in cache if not found add None
        self.location_cache[coordinates] = tmp
        return tmp
    
    def __is_valid_coordinate(self, lat, lon):

        """
        Checks if the coordinates lat, long are valid.

        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.

        Returns:
            bool: True if the coordinates are valid, otherwise False.
        """
        if isclose(lat, 0.0) and isclose(lon, 0.0):
            return False
        if not (-90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0):
            return False
        return True
        
    def __recoverable_location(self, lat, lon):
        """
        Determines if the given coordinates are recoverable based on predefined boundaries.

        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.

        Returns:
            bool: True if the location is recoverable, otherwise False.
        """
        if not self.__is_valid_coordinate(lat, lon):
            return False # Boundary Coordinate
        if 15.0 <= lat <= 75.0 and -168.0 <= lon <= -52.0:
            return False # North America
        elif -55.0 <= lat <= 12.0 and -82.0 <= lon <= -34.0:
            return False # South America
        elif 36.0 <= lat <= 71.0 and -10.0 <= lon <= 40.0:
            #if 27.0 <= lat <= 43.8 and -18.1 <= lon <= 4.3:
            #    return True # Spain
            #elif 41.3 <= lat <= 51.1 and -5.2 <= lon <= 9.6:
            #    return True # France
            #elif 47.3 <= lat <= 55.1 and 5.9 <= lon <= 15.1:
            #    return True # Germany
            #elif 45.8 <= lat <= 47.8 and 5.9 <= lon <= 10.5:
            #    return True # Switzerland
            #elif 49.9 <= lat <= 61.3 and -8.6 <= lon <= 1.8:
            #    return True # UK
            return True # Europe
        elif -35.0 <= lat <= 38.0 and -18.0 <= lon <= 52.0:
            return False # Africa
        elif -10.0 <= lat <= 81.0 and 26.0 <= lon <= 180.0:
            return False # Asia
        elif -50.0 <= lat <= -10.0 and 110.0 <= lon <= 180.0:
            return False # Oceania
        else:
            return False #Remote Area
    
    def __transform_classification_dimension(self, item):
        pass