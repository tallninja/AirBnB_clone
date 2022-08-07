#!/usr/bin/python3
"""user module
"""


import datetime
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """user model inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init method for user class used in instantiation
        """
        super().__init__(*args, **kwargs)
