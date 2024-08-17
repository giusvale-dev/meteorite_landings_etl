"""
DimensionLocationModel Class for Location Dimension

Author: Giuseppe Valente <valentepeppe@gmail.com>

Dependencies:

Usage:
    - Create a DimensionLocationModel instance
"""

class DimensionLocationModel:
    """
    Represents a geographical location with latitude, longitude, city, state, and country.

    Attributes:
        location (tuple): A tuple representing the geographical coordinates (latitude, longitude).
        city (str): The name of the city.
        state (str): The name of the state or province.
        country (str): The name of the country.
    """

    def __init__(self, latitude, longitude, city, state, country):

        """
        Initializes a DimensionLocationModel object with the specified latitude, longitude, city, state, and country.

        Args:
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            city (str): The city associated with the location.
            state (str): The state or province associated with the location.
            country (str): The country associated with the location.
        """

        self.location = (latitude, longitude)
        self.city = city
        self.state = state
        self.country = country

    def __eq__(self, other):

        """
        Compares the current DimensionLocationModel object with another object to check if they represent the same location.

        Args:
            other (DimensionLocationModel): Another instance of DimensionLocationModel to compare.

        Returns:
            bool: True if the locations (latitude and longitude) are the same, otherwise False.
        """
        if isinstance(other, DimensionLocationModel):
            return self.location[0] == other.location[0] and self.location[1] == other.location[1]
        return False

    def __hash__(self) -> int:
        """
         Generates the hash value for the DimensionLocationModel object.

         Returns:
            int: The hash value of the location (latitude and longitude).
        """
        return hash(self.location)