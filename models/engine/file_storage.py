#!/usr/bin/python3
"""
Module for working with the FileStorage class
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    An object file storage system is represented by this class.
    It is possible to serialize, store, and retrieve objects to
    and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}
    __instance = None

    def __init__(self):
        """
        Initializes the FileStorage instance.
        It loads the data into the __objects dictionary and populates it
        if the file.json file exists and if it does prints and empty dict
        """
        if not FileStorage.__instance:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r") as file:
                    serialized_data = json.load(file)
                    for key, obj_dict in serialized_data.items():
                        class_name, obj_id = key.split(".")
                        class_obj = eval(class_name)
                        obj = class_obj(**obj_dict)
                        self.__objects[key] = obj
            else:
                self.__objects = {}
            FileStorage.__instance = self

    def all(self):
        """
        Returns the __objects dictionary, which includes every item that
        has been stored.

        Returns: dict: An object dictionary with keys that follow the
        syntax "ClassName.object_id".
        """
        return self.__objects

    def new(self, in_obj):
        """
        introduces a new object into the dictionary of __objects.

        Args: obj (BaseModel): The item that has to be included in
            the dictionary.
        """
        key = f"{in_obj.__class__.__name__}.{in_obj.id}"
        self.__objects[key] = in_obj

    def save(self):
        """
        Stores the objects in the file.json file after serializing them
        from the __objects dictionary.
        """
        serialized_data = {}
        for key, in_obj in self.__objects.items():
            serialized_data[key] = in_obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_data, file)

    def reload(self):
        """
        loads the contents of the file again.JSON data set.
        Takes the serialized data from the file, deserializes it,
        and adds the deserialized objects to the __objects dictionary
        after clearing the dictionary.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                try:
                    serialized_data = json.load(file)
                    self.__objects = {}
                    for key, obj_dict in serialized_data.items():
                        class_name, obj_id = key.split(".")
                        class_obj = eval(class_name)
                        in_obj = class_obj(**obj_dict)
                        self.__objects[key] = in_obj
                except Exception:
                    pass
