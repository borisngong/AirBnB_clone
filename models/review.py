#!/usr/bin/python3
"""
A module for working with the review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    represents an evaluation or review of a location.
    """
    place_id = ""
    user_id = ""
    text = ""