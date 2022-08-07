#!/usr/bin/python3

from models.base_model import BaseModel

"""
models/place.py - defines a place
"""


class Place(BaseModel):
    """defines a place"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    ameamenity_ids = []
