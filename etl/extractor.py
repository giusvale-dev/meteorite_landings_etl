"""
Extractor Class for NASA Meteorite Landings API

Author: Giuseppe Valente <valentepeppe@gmail.com>

This module defines the Extractor class that handles data extraction from
NASA's Meteorite Landings API. The Extractor class includes methods to
retrieve and process meteorite landing data with error handling for
HTTP requests.

Dependencies:
- requests: For making HTTP requests to the NASA API.

Usage:
    - Create an instance of Extractor.
    - Use the get_data_from_nasa method to retrieve data from the API with specified offsets.
"""
import requests

class Extractor:
    """
    A class to handle data extraction from NASA's Meteorite Landings API.

    This class provides methods to retrieve and process meteorite landing data
    from NASA's open data API. It includes error handling for failed HTTP requests.
    """
    
    _NASA_API_ENDPOINT = "https://data.nasa.gov/resource/gh4g-9sfh.json?$limit=999"

    def __init__(self):
        """
        Initializes the Extractor class.
        """
        pass
    
    def get_data_from_nasa(self, offset):
        """
        Retrieves data from NASA's Meteorite Landings API with a given offset.

        This method constructs the request URL by appending the offset parameter to the base API endpoint,
        sends an HTTP GET request, and returns the JSON response if successful. 

        Parameters:
        - offset (int): The offset parameter to paginate through the API results.

        Returns:
        - list: A list of meteorite landing records in JSON format if the request is successful.
        - None: If the request fails or an error occurs, None is returned.

        Raises:
        - Exception: If an unexpected error occurs during the HTTP request.
        """
        response = requests.get("".join([self._NASA_API_ENDPOINT, "&$offset=", str(offset)]))
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON content into a Python dictionary
            return response.json()
        else:
            raise Exception(f"Failed to retrieve data: HTTP {response.status_code}")
            
    @property
    def NASA_API_ENDPOINT(self):
        """
        Returns the base URL for NASA's Meteorite Landings API.

        This property provides read-only access to the API endpoint URL.

        Returns:
        - str: The base URL of the NASA Meteorite Landings API.
        """
        return self._NASA_API_ENDPOINT