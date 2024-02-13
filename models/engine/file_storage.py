#!/usr/bin/python3
"""
Module for working with the FileStorage class
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    An object file storage system is represented by this class
    It is possible to serialize, store, and retrieve objects to
    and from a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary, which includes every item that
        has been stored. The object dictionary with keys that follow the
        syntax "ClassName.object_id"
        """
        return self.__objects

    def new(self, in_obj):
        """
        introduces a new object into the dictionary of __objects.

        Args:
            obj: The item that has to be included in
            the dictionary.
        """
        key = "{}.{}".format(in_obj.__class__.__name__, in_obj.id)
        self.__objects[key] = in_obj

    def save(self):
        """
        Stores the objects in the file.json file after serializing them
        from the __objects dictionary
        """
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_data, file)

    def reload(self):
        """
        loads the file's contents once more.JSON dataset.
        deserializes the serialized data from the file and,
        after the dictionary has been cleared, adds the deserialized
        objects to the __objects dictionary.
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    serialized_data = json.load(file)
                    for key, obj_dict in serialized_data.items():
                        target_class, obj_id = key.split(".")
                        if target_class == "User":
                            obj = User(**obj_dict)
                        elif target_class == "Place":
                            obj = Place(**obj_dict)
                        elif target_class == "State":
                            obj = State(**obj_dict)
                        elif target_class == "City":
                            obj = City(**obj_dict)
                        elif target_class == "Amenity":
                            obj = Amenity(**obj_dict)
                        elif target_class == "Review":
                            obj = Review(**obj_dict)
                        self.__objects[key] = obj
            except Exception:
                pass
