#!/usr/bin/python3
"""
A module for working with class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
     symbolizes a city.

    Attributes:
        state_id (str): The city's ID inside the state.
        name (str): The city's name.
    """
    state_id = ""
    name = ""