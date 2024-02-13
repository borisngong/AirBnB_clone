#!/usr/bin/python3
"""
Module for creating and working with User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class responsible for representing User objects
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
