#!/usr/bin/python3

import json
import os
from models.classes import classes
from models.base_model import BaseModel

"""
models/engine/file_storage.py - file storage engine
"""


class FileStorage:
    """
    serializes instances to JSON file and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects_dict = {}
        for k, v in self.__objects.items():
            objects_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(objects_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        objects_dict = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                objects_dict = json.load(json_file)
        for k, v in objects_dict.items():
            self.__objects[k] = classes[v['__class__']](**v)
