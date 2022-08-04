#!/usr/bin/python3
"""
Module containing FileStorage object definition
"""
from .json_helpers.save_to_json_file import save_to_json_file
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Definition of the FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dics = dict(self.__objects)
        for k, v in dics.items():
            if type(v) is not dict:
                dics[k] = v.to_dict()
        save_to_json_file(dics, self.__file_path)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:

            with open(self.__file_path, 'r', encoding="utf-8") as j:
                fl = j.read()
                if fl:
                    objs = json.loads(fl)
                else:
                    objs = {}
        except FileNotFoundError:
            objs = {}
        for k, v in objs.items():
            self.__objects[k] = BaseModel(**v)
