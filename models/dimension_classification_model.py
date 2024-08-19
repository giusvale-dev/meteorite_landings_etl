"""
DimensionClassificationModel Class for represents the classification of a meteorite in the data model.

Author: Giuseppe Valente <valentepeppe@gmail.com>

Usage:
    - Create an instance of DimensionClassificationModel.
"""
class DimensionClassificationModel:
    """
    Represents the classification of a meteorite in the data model.

    Attributes:
        group (str): The classification group of the meteorite.
        clan (str): The clan classification of the meteorite.
        clazz (str): The class classification of the meteorite.
        chemical_composition (str): The chemical composition of the meteorite.
        material (str): The material type of the meteorite.
    """

    def __init__(self, group=None, clan=None, clazz=None, chemical_composition=None, material=None):
        """
        Initialize a DimensionClassificationModel instance.

        :param group: The classification group of the meteorite
        :param clan: The clan classification of the meteorite
        :param clazz: The class classification of the meteorite
        :param chemical_composition: The chemical composition of the meteorite
        :param material: The material type of the meteorite
        """
        self.group = group
        self.clan = clan
        self.clazz = clazz
        self.chemical_composition = chemical_composition
        self.material = material