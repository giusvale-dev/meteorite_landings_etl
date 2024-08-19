"""
Loader Class for implement the loader process 

Author: Giuseppe Valente <valentepeppe@gmail.com>

Usage:
    - Create an instance of Loader.
    - Call method save_data using with
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm.persistence import Meteorite
from orm.persistence import Classification
from orm.persistence import Date
from orm.persistence import Location
from models.meteorite_model import MeteoriteModel
from models.dimension_location_model import DimensionLocationModel
from models.dimension_date_model import DimensionDateModel
from models.dimension_classification_model import DimensionClassificationModel
from datetime import datetime
from typing import List
import os

class Loader:

    # Environment variable for database url
    DATABASE_URL = os.getenv("DATABASE_URL")

    def __init__(self, data: List[MeteoriteModel]):

        """
        Initialize the Loader instance.

        :param data: A list of MeteoriteModel instances to be loaded into the database.
        """
        self.transformed_data = data
        self.__engine = create_engine(self.DATABASE_URL)
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = None

    def __enter__(self):
        """
        Start a new database session and return the Loader instance.
        This method is called when the loader using with
        return: The current instance of the Loader.
        """
        self.__session = self.__Session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):

        """
        Close the database session and handle exceptions.
        
        This method is called when with finishs the execution
        """
        if self.__session:
            self.__session.close()

    def __build_location(self, raw_data: DimensionLocationModel):
        """
        Convert DimensionLocationModel to Location entity.

        :param raw_data: An instance of DimensionLocationModel.
        :return: An instance of Location entity.
        """
        tmp = Location()
        tmp.city = raw_data.city
        tmp.country = raw_data.country
        tmp.state = raw_data.state
        tmp.latitude = raw_data.location[0]
        tmp.longitude = raw_data.location[1]
        return tmp
    
    def __build_date(self, raw_data: DimensionDateModel):
        """
        Convert DimensionDateModel to Date entity.

        :param raw_data: An instance of DimensionDateModel.
        :return: An instance of Date entity.
        """
        tmp = Date()
        tmp.year = raw_data.year
        tmp.month = raw_data.month
        tmp.quarter = raw_data.quarter
        tmp.date = datetime.fromtimestamp(raw_data.timestamp)
        return tmp
    
    def __build_classification(self, raw_data: DimensionClassificationModel):
        """
        Convert DimensionClassificationModel to Classification entity.

        :param raw_data: An instance of DimensionClassificationModel.
        :return: An instance of Classification entity.
        """
        tmp = Classification()
        tmp.chemical_composition = raw_data.chemical_composition
        tmp.classification = raw_data.group
        tmp.material_type = raw_data.material
        tmp.clan = raw_data.clan
        tmp.clazz = raw_data.clazz
        return tmp
    
    def save_data(self):
        """
        Load the transformed data into the database. Each MeteoriteModel is converted to
        a Meteorite entity with associated Classification, Date, and Location entities.
        """
        if not self.__session:
            raise Exception("Session not started. ")
        try:
            for record in self.transformed_data:
                m = Meteorite()
                m.classification = self.__build_classification(record.dimensionClassificationModel)
                m.date = self.__build_date(record.dimensionDateModel)
                m.location = self.__build_location(record.dimensionLocationModel)
                m.mass = record.mass
                self.__session.add(m)
            self.__session.commit() # Commit changes in atomic way
        except Exception as e:
            self.__session.rollback()
            raise e