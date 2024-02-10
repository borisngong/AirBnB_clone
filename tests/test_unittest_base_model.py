#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        Assemble the test fixture. Every test method is called after this one
        For testing purposes, it creates an instance of the BaseModel class
        """
        self.boro_model = BaseModel()

    def test_if_id_is_string(self):
        """
        Verify whether the BaseModel instance's 'id' field is of type string.
        """
        self.assertIsInstance(self.boro_model.id, str)

    def test_if_created_at_is_datetime(self):
        """
        Verify whether the BaseModel instance's 'created_at' field is of type
        datetime
        """
        self.assertIsInstance(self.boro_model.created_at, datetime)

    def test_if_updated_at_is_datetime(self):
        """
        Verify whether the BaseModel instance's 'updated_at' field is of type
        datetime
        """
        self.assertIsInstance(self.boro_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Verify whether the BaseModel instance's "updated_at" attribute is
        updated by the "save" method.
        """
        former_updated_at = self.boro_model.updated_at
        self.boro_model.save()
        self.assertNotEqual(former_updated_at, self.boro_model.updated_at)
        self.assertGreater(self.boro_model.updated_at, former_updated_at)

    def test_to_dict_returns_dict(self):
        """
        Verify whether the BaseModel instance's dictionary representation is
        returned by the 'to_dict' method.
        """
        boro_dict = self.boro_model.to_dict()
        self.assertIsInstance(boro_dict, dict)
        self.assertIn('id', boro_dict)
        self.assertIn('created_at', boro_dict)
        self.assertIn('updated_at', boro_dict)


if __name__ == '__main__':
    unittest.main()
