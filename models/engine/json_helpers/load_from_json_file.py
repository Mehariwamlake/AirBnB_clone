#!/usr/bin/python3
"""
Module contains the definition of "save_to_json_file" function
"""
from .from_json_string import from_json_string


def load_from_json_file(filename):
    """
    creates an Object from a json file
    """
    with open(filename, encoding="utf-8") as my_file:
        json_string = my_file.read()
        return from_json_string(json_string)
