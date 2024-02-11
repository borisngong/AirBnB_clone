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
        boro = BaseModel()

        self.assertIsNotNone(boro.id)
        self.assertIsNotNone(boro.created_at)
        self.assertIsNotNone(boro.updated_at)

    def test_id_is_string(self):
        """
        Verify whether the BaseModel instance's 'id' field is of
        type string.
        """
        boro = BaseModel()

        self.assertIsInstance(boro.id, str)

    def test_created_at_is_datetime(self):
        """
        Verify whether the BaseModel instance's 'created_at' field
        is of type datetime.
        """
        boro = BaseModel()

        self.assertIsInstance(boro.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Verify whether the BaseModel instance's 'updated_at' field is of
        type datetime.
        """
        boro = BaseModel()

        self.assertIsInstance(boro.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Verify whether the BaseModel instance's "updated_at" attribute is
        updated by the "save" method.
        """
        boro = BaseModel()

        former_updated_at = boro.updated_at
        boro.save()
        self.assertNotEqual(former_updated_at, boro.updated_at)
        self.assertGreater(boro.updated_at, former_updated_at)

    def test_to_dict_returns_dict(self):
        """
        Verify whether the BaseModel instance's dictionary representation is
        returned by the 'to_dict' method.
        """
        boro = BaseModel()

        boro_dict = boro.to_dict()
        self.assertIsInstance(boro_dict, dict)
        self.assertIn('id', boro_dict)
        self.assertIn('created_at', boro_dict)
        self.assertIn('updated_at', boro_dict)


if __name__ == '__main__':
    unittest.main()

