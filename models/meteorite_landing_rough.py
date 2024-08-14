"""
MeteoriteLandingRough Class for NASA Meteorite Landings API

Author: Giuseppe Valente <valentepeppe@gmail.com>

This module defines the MeteoriteLandingRough class that is responsible to map the json raw data from NASA

Usage:
    - Create an instance of MeteoriteLandingRough.
"""
class MeteoriteLandingRough:

    """
    Represents a meteorite landing record with various attributes related to the meteorite's characteristics
    and landing details.

    This class is used to encapsulate information about a meteorite, including its unique identifier, name,
    classification, mass, fall status, year of fall or discovery, and its geographical coordinates.

    Attributes:
        id (int): The unique identifier for the meteorite.
        name (str): The name of the meteorite.
        name_type (str): The type of name (e.g., 'Relict' or 'Valid') for the meteorite.
        recclass (str): The classification of the meteorite.
        mass (float): The mass of the meteorite in grams.
        fall (str): The fall status of the meteorite, either 'Fell' (for observed falls) or 'Found' (for discovered meteorites).
        year (str): The year the meteorite fell or was discovered, represented as a string.
        reclat (float): The latitude of the meteorite landing location in decimal degrees.
        reclong (float): The longitude of the meteorite landing location in decimal degrees.
    """   
    def __init__(self, id, name, name_type, recclass, mass, fall, year, reclat, reclong):
        """
        Initializes a new instance of the MeteoriteLandingRough class.

        Parameters:
            id (int): The unique identifier for the meteorite.
            name (str): The name of the meteorite.
            name_type (str): The type of name for the meteorite (e.g., 'Relict' or 'Valid').
            recclass (str): The classification of the meteorite.
            mass (float): The mass of the meteorite in grams.
            fall (str): The fall status of the meteorite ('Fell' or 'Found').
            year (str): The year the meteorite fell or was discovered.
            reclat (float): The latitude of the meteorite landing location in decimal degrees.
            reclong (float): The longitude of the meteorite landing location in decimal degrees.
        """
        self.id = id
        self.name = name
        self.name_type = name_type
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong