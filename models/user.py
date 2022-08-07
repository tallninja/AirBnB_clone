#!/usr/bin/python3

from models.base_model import BaseModel

"""
models/user.py - defines a user
"""


class User(BaseModel):
    """defines a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
