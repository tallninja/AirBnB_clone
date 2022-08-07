#!/usr/bin/python3
"""Test State"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Teststate(unittest.TestCase):
    """
    Unittests for the State class.
    """

    def test_class(self):
        """
        Tests if class is named correctly.
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")
