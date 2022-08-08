#!/usr/bin/python3
"""
This module contains the definition of the Amenity class
that inherits BaseModel.
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a Amenity object
        """
        BaseModel.__init__(self, *args, **kwargs)
