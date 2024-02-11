#!/usr/bin/python3

""""""
import unittest
from unittest.mock import patch
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up the file after each test
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_reload_method(self):
        # Create a new object
        my_model = BaseModel()
        my_model.id = "123"  # Set the ID to '123'
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        # Add the object to storage
        self.storage.new(my_model)

        # Save the objects to the JSON file
        self.storage.save()

        # Reload the objects from the JSON file
        self.storage.reload()

        # Retrieve all objects from storage
        all_objs = self.storage.all()

        # Verify that the reloaded object exists in storage with the correct ID
        expected_id = f"{my_model.__class__.__name__}.123"  # Expected ID
        self.assertIn(expected_id, all_objs)

        # Retrieve the reloaded object and compare its attributes
        reloaded_model = all_objs[expected_id]
        self.assertEqual(reloaded_model.name, "My_First_Model")
        self.assertEqual(reloaded_model.my_number, 89)


if __name__ == '__main__':
    unittest.main()
