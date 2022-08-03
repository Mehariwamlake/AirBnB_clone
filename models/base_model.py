#!/usr/bin/python3
""" Module for Base """
import uuid
import datetime
import models

format_dt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """ Basemodel class """
    def __init__(self, *args, **kwargs):
        """ Initialization of Database """
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)