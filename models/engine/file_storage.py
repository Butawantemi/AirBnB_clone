#!/usr/bin/python3
"""File Storage Class"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This class provides a file storage module."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of objects."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """Serializes the objects dictionary to a JSON file."""
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(my_dict, myfile)

    def reload(self):
        """Deserializes the JSON file and updates the objects dictionary."""
        try:
            with open(FileStorage.__file_path, "r") as myfile:
                a_dict = json.load(myfile)

            for key, value in a_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
