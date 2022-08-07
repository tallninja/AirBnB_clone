#!/usr/bin/python3
"""state module
"""


import datetime
import uuid
from models.base_model import BaseModel


class State(BaseModel):
    """state model inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """init method for state class used in instantiation
        """
        super().__init__(*args, **kwargs)
