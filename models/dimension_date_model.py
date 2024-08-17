"""
DimensionDateModel Class for Date Dimension

Author: Giuseppe Valente <valentepeppe@gmail.com>

Dependencies:
    - datetime

Usage:
    - Create a DimensionDateModel instance
"""
from datetime import datetime

class DimensionDateModel:

    """
    Represents a Date with year, month, quarter and timestamp.

    Attributes:
        year (int): The numerical year.
        month (int): The numerical month
        quarter (int): The numerical quarter
        timestamp (float): The timestamp.
    """

    def __init__(self, timestamp: str):
        """
        Initializes a DimensionDateModel object starting from the timestamp in str format.
        If the timestamp cannot be convert returns None
        Args:
            timestamp (str): The timestamp in str
        """
        try:
            date_obj = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
            # Extract the year
            self.year = date_obj.year
            # Extract the month
            self.month = date_obj.month
            # Calculate the quarter
            self.quarter = (self.month - 1) // 3 + 1
            # Get the timestamp
            self.timestamp = date_obj.timestamp()

        except ValueError as ve:
            print(f"Error: {str(ve)}")
            return None