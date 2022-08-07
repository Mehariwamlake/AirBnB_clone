#!/usr/bin/python3
""" Module User """
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a subclass of BaseModel """
    password = ""
    email = ""
    first_name = ""
    last_name = ""
