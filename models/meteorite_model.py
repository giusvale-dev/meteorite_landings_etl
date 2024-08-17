"""
MeteoriteModel Class for represents the Meteorite with all related Dimensions

Author: Giuseppe Valente <valentepeppe@gmail.com>

Usage:
    - Create an instance of MeteoriteModel.
"""

from models.dimension_date_model import DimensionDateModel
from models.dimension_location_model import DimensionLocationModel
class MeteoriteModel:

    """
    Represents a meteorite containing all related dimensions.

    This class is used to encapsulate information about a meteorite with the dimensions analyzed in the analysis phase.

    Attributes:
        dimensionDateModel (DimensionDateModel): The model releated to the Date dimension
        dimensionLocationModel (DimensionLocationModel): The model releated to the Location dimension
        mass (float): The mass (in grams) of the meteorite
    """ 
    
    def __init__(self, dimensionDateModel: DimensionDateModel, mass, dimensionLocationModel: DimensionLocationModel):

        """
        Initializes a new instance of the MeteoriteModel class.

        Parameters:
            dimensionDateModel (DimensionDateModel): The model releated to the Date dimension
            dimensionLocationModel (DimensionLocationModel): The model releated to the Location dimension
            mass (float): The mass (in grams) of the meteorite
        """
        self.dimensionDateModel = dimensionDateModel
        self.dimensionLocationModel = dimensionLocationModel
        self.mass = mass