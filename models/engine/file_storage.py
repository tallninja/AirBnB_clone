#!/usr/bin/python3
"""
module for serializing and deserializing object to file storage
"""
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    FileStorage class for serializing and deserializing objects
    into and from files respectively
    """
    engine_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.getcwd()
    __file_path = parent_directory + '/file.json'
    __objects = dict()

    def __init__(self):
        """instantiation method for class
        """
        pass

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        # TODO not sure if this check is needed for holberton checker
        try:
            obj_d = obj.to_dict()
        except Exception as e:
            raise TypeError('object passed to filestorage has no to_dict()')
        key = obj_d['__class__'] + '.' + str(obj_d['id'])
        self.__objects[key] = obj

    def delete(self, obj):
        """deletes obj from __objects
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception as e:
            return False

    def save(self):
        """serializes the __objects to the JSON file
            -> path (__file_path)
        """
        json_dump = str({k: v.to_dict() for (k, v) in self.__objects.items()})
        json_dump = json_dump.replace('\'', '"')
        with open(self.__file_path, 'w', encoding='utf-8') as myFile:
            myFile.write(json_dump)

    def reload(self):
        """deserializes the JSON file to __objects
            -> path (__file_path)
           ONLY if it exists, no exceptions are raised
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except Exception as e:
            return
        objects = eval(my_obj_dump)
        for (k, v) in objects.items():
            objects[k] = eval(k.split('.')[0] + '(**v)')
        self.__objects = objects

    def get_filepath(self):
        """get filepath for JSON file
        """
        return self.__file_path
