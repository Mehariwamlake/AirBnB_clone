#!/usr/bin/python3
""" Module base_model
Contains BaseModel class
"""

import uuid
from datetime import datetime
import models
t = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Represent a class BaseModel that defines
    all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """Initialises data """
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, "created_at") and\
                   type(self.created_at) is str:
                    self.created_at = datetime.\
                        strptime(kwargs["created_at"], t)
                if hasattr(self, "updated_at") and\
                   type(self.updated_at) is str:
                    self.updated_at = datetime.\
                        strptime(kwargs["updated_at"], t)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a readable string representation
        of an instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Updates public attr updated_at with current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns dict with all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
