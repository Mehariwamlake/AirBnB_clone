#!/usr/bin/python3
"""
This module contains the definition of the State class
that inherits BaseModel.
"""
from .base_model import BaseModel


class State(BaseModel):
    """

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a State object
        """
        BaseModel.__init__(self, *args, **kwargs)
