#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        Test the initialization of a BaseModel instance.
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.created_at)

    def test_(self):
        """
        Verify whether the BaseModel instance's 'id' field is of type string.
        """
        my_model = BaseModel()

        self.assertIsInstance(my_model.id, str)

    def test_if_created_at_is_datetime(self):
        """
        Verify whether the BaseModel instance's 'created_at' field is of type datetime.
        """
        my_model = BaseModel()

        self.assertIsInstance(my_model.created_at, datetime)

    def test_if_updated_at_is_datetime(self):
        """
        Verify whether the BaseModel instance's 'updated_at' field is of type datetime.
        """
        my_model = BaseModel()

        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Verify whether the BaseModel instance's "updated_at" attribute is updated by the "save" method.
        """
        my_model = BaseModel()

        former_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(former_updated_at, my_model.updated_at)
        self.assertGreater(my_model.updated_at, former_updated_at)

    def test_to_dict_returns_dict(self):
        """
        Verify whether the BaseModel instance's dictionary representation is returned by the 'to_dict' method.
        """
        my_model = BaseModel()

        boro_dict = my_model.to_dict()
        self.assertIsInstance(boro_dict, dict)
        self.assertIn('id', boro_dict)
        self.assertIn('created_at', boro_dict)
        self.assertIn('updated_at', boro_dict)


if __name__ == '__main__':
    unittest.main()
