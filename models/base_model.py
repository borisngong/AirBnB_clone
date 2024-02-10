#!/usr/bin/python3
"""
This module is for working with the BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A basic model with shared properties and methods that are utilized by
    numerous models is represented by the BaseModel class.

    """
    def __init__(self):
        """
        A constructor for classes that initializes a new BaseModel instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns the BaseModel instance represented in a string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id,
                                         self.__dict__)

    def save(self):
        """
        Adds the current datetime to the updated_at attribute
        To show that the instance has been updated, call this method
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Responsible for creating a dictionary from the attributes of a
        BaseModel instance
        """
        data_instance_dict = self.__dict__.copy()
        data_instance_dict['__class__'] = self.__class__.__name__
        data_instance_dict['created_at'] = self.created_at.isoformat()
        data_instance_dict['updated_at'] = self.updated_at.isoformat()

        return data_instance_dict
