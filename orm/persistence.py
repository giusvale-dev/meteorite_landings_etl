"""
Entity classes used to manage database data 

Author: Giuseppe Valente <valentepeppe@gmail.com>

"""
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Sequence, Double, DateTime
from sqlalchemy.orm import declarative_base, relationship, Mapped
from sqlalchemy.orm import composite, mapped_column


Base = declarative_base()

class Classification(Base):
    """
    Represents the classification of a meteorite, including its material type, chemical composition,
    and other classification attributes.

    Attributes:
        id (int): Primary key, unique identifier for the classification.
        classification (str): The classification string from NASA or another source.
        material_type (str): The type of material (e.g., 'STONY', 'IRON').
        chemical_composition (str): Chemical composition of the meteorite.
        clan (str): Sub-category or clan of the classification.
        clazz (str): Class of the meteorite.
    """
    __tablename__ = 'classification'
    __table_args__ = {'schema': 'public'}
    
    id = Column(Integer, Sequence('classification_id_seq'), primary_key=True, autoincrement=True)
    classification = Column(String(255))
    material_type = Column(String(255))
    chemical_composition = Column(String(255))
    clan = Column(String(255))
    clazz = Column(String(255))

    def __repr__(self):
        return f"<Classification(id={self.id}, classification={self.classification})>"

class Date(Base):
    """
    Represents a date record used to track when a meteorite was observed or collected.

    Attributes:
        id (int): Primary key, unique identifier for the date.
        date (datetime): The full date of the event.
        month (int): Month of the event.
        quarter (int): Quarter of the year when the event occurred.
        year (int): Year of the event.
    """
    __tablename__ = 'date'
    __table_args__ = {'schema': 'public'}
    
    id = Column(Integer, Sequence('date_id_seq'), primary_key=True, autoincrement=True)
    date = Column(DateTime)
    month = Column(Integer)
    quarter = Column(Integer)
    year = Column(Integer)

    def __repr__(self):
        return f"<Date(id={self.id}, year={self.year})>"

class Location(Base):
    """
    Represents the location where a meteorite was found.

    Attributes:
        id (int): Primary key, unique identifier for the location.
        latitude (float): Latitude coordinate of the location.
        longitude (float): Longitude coordinate of the location.
        city (str): City where the meteorite was found.
        state (str): State where the meteorite was found.
        country (str): Country where the meteorite was found.
    """
    __tablename__ = 'location'
    __table_args__ = {'schema': 'public'}
    
    id = Column(Integer, Sequence('location_id_seq'), primary_key=True, autoincrement=True)
    latitude = Column(Double)
    longitude = Column(Double)
    city = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))

    def __repr__(self):
        return f"<Location(id={self.id}, city={self.city})>"

class Meteorite(Base):
    """
    Represents a meteorite specimen including its mass and associated metadata such as classification,
    location, and date.

    Attributes:
        id_location (int): Foreign key linking to the Location table.
        id_classification (int): Foreign key linking to the Classification table.
        id_date (int): Foreign key linking to the Date table.
        mass (float): The mass of the meteorite in grams.
    """
    __tablename__ = 'meteorite'
    __table_args__ = {'schema': 'public'}
    
    id_location = Column(Integer, ForeignKey('public.location.id'), primary_key=True)
    id_classification = Column(Integer, ForeignKey('public.classification.id'), primary_key=True)
    id_date = Column(Integer, ForeignKey('public.date.id'), primary_key=True)
    mass = Column(Float, nullable=False)
    
    # Relationships
    location = relationship("Location", backref="meteorites")
    classification = relationship("Classification", backref="meteorites")
    date = relationship("Date", backref="meteorites")

    def __repr__(self):
        return f"<Meteorite(id_location={self.id_location}, id_classification={self.id_classification}, id_date={self.id_date}, mass={self.mass})>"