#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_data, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    serialized_data = json.load(file)
                    for key, obj_dict in serialized_data.items():
                        class_name, obj_id = key.split(".")
                        if class_name == User:
                            obj = User(**obj_dict)
                        else:
                            class_obj = eval(class_name)
                        obj = class_obj(**obj_dict)
                        self.__objects[key] = obj
            except Exception:
                pass
