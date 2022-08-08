#!/usr/bin/python3
"""
This module contains the definition of the Place class
that inherits BaseModel.
"""
from .base_model import BaseModel


class Place(BaseModel):
    """

    """
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
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialize a Place object
        """
        BaseModel.__init__(self, *args, **kwargs)
