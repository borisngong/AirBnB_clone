#!/usr/bin/python3
"""
Module for working with class amenity
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    symbolizes an amenity.

    Attributes:
    name (str): Amenity's name
    """
    name = ""