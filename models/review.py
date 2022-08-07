#!/usr/bin/python3
"""review module
"""


import datetime
import uuid
from models.base_model import BaseModel


class Review(BaseModel):
    """review model inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method for review class used in instantiation
        """
        super().__init__(*args, **kwargs)
