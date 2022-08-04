#!/usr/bin/python3
"""
This module defines BaseModel which is a base model for all
AIRBNB project objects
"""
from uuid import uuid4
import models
from datetime import datetime


datetime_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Definition of the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel object
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, datetime_format)

                if key not in ["__class__"]:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method that sets the time object was updated
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Generates a dictionary representation of the object
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
