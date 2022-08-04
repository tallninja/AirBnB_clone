#!/usr/bin/env python3

import json
import uuid
from datetime import datetime
"""
module models/base_model.py - base model
"""


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """constructor"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """informal string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        curr_dict = self.__dict__.copy()
        curr_dict.update({"__class__": self.__class__.__name__})
        curr_dict.update({"created_at": self.created_at.isoformat()})
        curr_dict.update({"updated_at": self.updated_at.isoformat()})
        return curr_dict
