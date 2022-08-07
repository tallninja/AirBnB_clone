#!/usr/bin/python3
"""amenity module
"""


import datetime
import uuid
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity model inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """init method for amenity class used in instantiation
        """
        super().__init__(*args, **kwargs)
