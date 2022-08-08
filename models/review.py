#!/usr/bin/python3
"""
This module contains the definition of the Review class
that inherits BaseModel.
"""
from .base_model import BaseModel


class Review(BaseModel):
    """

    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a Review object
        """
        BaseModel.__init__(self, *args, **kwargs)
