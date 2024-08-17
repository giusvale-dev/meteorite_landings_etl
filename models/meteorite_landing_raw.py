"""
MeteoriteLandingRaw Class for NASA Meteorite Landings API

Author: Giuseppe Valente <valentepeppe@gmail.com>

This module defines the MeteoriteLandingRaw class that is responsible to map the json raw data from NASA

Usage:
    - Create an instance of MeteoriteLandingRaw.
"""
class MeteoriteLandingRaw:

    """
    Represents a meteorite landing record with various attributes related to the meteorite's characteristics
    and landing details.

    This class is used to encapsulate information about a meteorite, including its unique name,
    classification, mass, year of fall or discovery, and its geographical coordinates.

    Attributes:
        recclass (str): The classification of the meteorite.
        mass (float): The mass of the meteorite in grams.
        year (str): The year the meteorite fell or was discovered, represented as a string.
        reclat (float): The latitude of the meteorite landing location in decimal degrees.
        reclong (float): The longitude of the meteorite landing location in decimal degrees.
    """   
    def __init__(self, name, recclass, mass, year, reclat, reclong):
        """
        Initializes a new instance of the MeteoriteLandingRaw class.

        Parameters:
            recclass (str): The classification of the meteorite.
            mass (float): The mass of the meteorite in grams.
            year (str): The year the meteorite fell or was discovered.
            reclat (float): The latitude of the meteorite landing location in decimal degrees.
            reclong (float): The longitude of the meteorite landing location in decimal degrees.
        """
        self.recclass = recclass
        self.mass = mass
        self.year = year
        self.reclat = reclat
        self.reclong = reclong