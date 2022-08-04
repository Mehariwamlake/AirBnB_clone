#!/usr/bin/python3
"""
Module for the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel,}

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand processor definition for HBNB project
    """

    prompt = '(hbnb) '


    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def do_create(self, obj_str):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not obj_str:
            print("** class name missing **")
        elif obj_str not in classes:
            print("** class doesn't exist **")
        else:
            new_obj = classes[obj_str]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, id_str):
        """
        Prints the string representation of an instance 
        based on the class name and id. 
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = id_str.split(" ")
        if not id_str:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = ".".join(args)
            obj = all_objs.get(key)
            print(obj) if obj else print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
