#!/usr/bin/python3
"""
This module contains the definition of the City class
that inherits BaseModel.
"""
from .base_model import BaseModel


class City(BaseModel):
    """

    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a City object
        """
        BaseModel.__init__(self, *args, **kwargs)
