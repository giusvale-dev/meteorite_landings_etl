"""
MeteoriteType Class to classify meteorites based on NASA classification strings.

Author: Giuseppe Valente <valentepeppe@gmail.com>

Usage:
    - Create an instance of DimensionClassificationModel.
"""
from models.dimension_classification_model import DimensionClassificationModel
class MeteoriteType:

    """
    Provides methods to classify meteorites based on NASA classification strings.

    This class includes static methods to generate `DimensionClassificationModel`
    instances for different types of meteorites: Primitive Achondrites, Chondrites,
    and Achondrites.
    """

    @staticmethod
    def primitive_achonrdites(nasa_classification:str):
    
        classification_model = DimensionClassificationModel()
        if(nasa_classification.upper().startswith("URE")):
            classification_model.material = "STONY"
            classification_model.group = "URE"
            classification_model.chemical_composition = "PRIMITIVE_ACHONDRITES"
            return classification_model
        elif(nasa_classification.upper().startswith("BRA")):
            classification_model.material = "STONY"
            classification_model.group = "BRA"
            classification_model.chemical_composition = "PRIMITIVE_ACHONDRITES"
            return classification_model
        elif(nasa_classification.upper().startswith("ACA")):
            classification_model.material = "STONY"
            classification_model.group = "ACA"
            classification_model.chemical_composition = "PRIMITIVE_ACHONDRITES"
            classification_model.clan = "ACA-LOD"
            return classification_model
        elif(nasa_classification.upper().startswith("LOD")):
            classification_model.material = "STONY"
            classification_model.group = "LOD"
            classification_model.chemical_composition = "PRIMITIVE_ACHONDRITES"
            classification_model.clan = "ACA-LOD"
            return classification_model
        elif(nasa_classification.upper().startswith("WIN")):
            classification_model.material = "STONY"
            classification_model.group = "WIN"
            classification_model.chemical_composition = "PRIMITIVE_ACHONDRITES"
            classification_model.clan = "WIN-IAB-IICD"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IAB")):
            classification_model.material = "IRON"
            classification_model.group = "IAB"
            classification_model.chemical_composition = "PRIMITIVE_ACHONDRITES"
            classification_model.clan = "WIN-IAB-IICD"
            return classification_model
        else:
            return None
        
    @staticmethod
    def chondrites(nasa_classification:str):

        classification_model = DimensionClassificationModel()
        if(nasa_classification.upper().startswith("CI")):
            classification_model.group = "CI"
            classification_model.clan = "CI"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CM")):
            classification_model.group = "CM"
            classification_model.clan = "CM-CO"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CO")):
            classification_model.group = "CO"
            classification_model.clan = "CM-CO"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CV")):
            classification_model.group = "CV"
            classification_model.clan = "CV-CK"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CK")):
            classification_model.group = "CK"
            classification_model.clan = "CV-CK"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CR")):
            classification_model.group = "CR"
            classification_model.clan = "CR-CLAN"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CH")):
            classification_model.group = "CH"
            classification_model.clan = "CR-CLAN"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("CB")):
            classification_model.group = "CB"
            classification_model.clan = "CR-CLAN"
            classification_model.clazz = "C"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("H") and nasa_classification.upper() != "HOWARDITE"):
            classification_model.group = "H"
            classification_model.clan = "H-L-LL"
            classification_model.clazz = "O"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("L") and not nasa_classification.upper().startswith("LL")):
            classification_model.group = "L"
            classification_model.clan = "H-L-LL"
            classification_model.clazz = "O"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("LL")):
            classification_model.group = "LL"
            classification_model.clan = "H-L-LL"
            classification_model.clazz = "O"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("EH")):
            classification_model.group = "EH"
            classification_model.clan = "EH-EL"
            classification_model.clazz = "E"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("EL")):
            classification_model.group = "EL"
            classification_model.clan = "EH-EL"
            classification_model.clazz = "E"
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("R") and not nasa_classification.upper().startswith("RE")):
            classification_model.group = "R"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("K")):
            classification_model.group = "K"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "CHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        else:
            return None
    
    @staticmethod
    def achonrdites(nasa_classification:str):

        classification_model = DimensionClassificationModel()
        if(nasa_classification.upper().startswith("ANG")):
            classification_model.group = "ANG"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("AUB")):
            classification_model.group = "AUB"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("EUC")):
            classification_model.group = "EUC"
            classification_model.clan = "VESTA"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("DIO")):
            classification_model.group = "DIO"
            classification_model.clan = "VESTA"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("HOW")):
            classification_model.group = "HOW"
            classification_model.clan = "VESTA"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif(nasa_classification.upper().startswith("MES")):
            classification_model.group = "MES"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY-IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("PAL")):
            classification_model.group = "PAL"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY-IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IC")):
            classification_model.group = "IRON, IC"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IIAB")):
            classification_model.group = "IRON, IIAB"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IIC")):
            classification_model.group = "IRON, IIC"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IID")):
            classification_model.group = "IRON, IID"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IIE")):
            classification_model.group = "IRON, IIE"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IIIAB")):
            classification_model.group = "IRON, IIIAB"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IIIE")):
            classification_model.group = "IRON, IIIE"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IIIF")):
            classification_model.group = "IRON, IIIF"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IVA")):
            classification_model.group = "IRON, IVA"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif(nasa_classification.upper().startswith("IRON, IVB")):
            classification_model.group = "IRON, IVB"
            classification_model.clan = None
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "IRON"
            return classification_model
        elif("SHE" in nasa_classification.upper()):
            classification_model.group = "SHE"
            classification_model.clan = "MARS"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif("NAK" in nasa_classification.upper()):
            classification_model.group = "NAK"
            classification_model.clan = "MARS"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif("CHA" in nasa_classification.upper()):
            classification_model.group = "CHA"
            classification_model.clan = "MARS"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        elif("OPX" in nasa_classification.upper()):
            classification_model.group = "OPX"
            classification_model.clan = "MARS"
            classification_model.clazz = None
            classification_model.chemical_composition = "ACHONDRITES"
            classification_model.material = "STONY"
            return classification_model
        else:
            return None