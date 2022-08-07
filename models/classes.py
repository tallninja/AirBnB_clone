#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
models/classes.py - contains a dictionary of all the classes
"""


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City
           "Amenity": Amenity, "Place": Place, "Review": Review}
