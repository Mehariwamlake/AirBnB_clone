#!/usr/bin/python3
"""
Program that contains the entry point of the command interpreter
"""

import cmd
import models
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "City": City,
               "Amenity": Amenity, "Place": Place,
               "Review": Review, "State": State}

    def emptyline(self):
        """ An empty line + ENTER shouldn't execute anything """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create a instance of basemodel, save it"""
        if line:
            if line in HBNBCommand.classes:
                class_to_ins = HBNBCommand.classes.get(line)
                new_instance = class_to_ins()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_show(self, line):
        """
        Prints the string representation of
        a instance based on the class name and id
        """
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list_line[1] not in \
                models.storage.all().keys():
            print("** no instance found **")
        else:
            obj = models.storage.all().get(list_line[0] + '.' + list_line[1])
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list_line[1] not in \
                models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(list_line[0] + '.' + list_line[1], None)
            models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        list_line = line.split(' ')
        string = ""
        list_all = []
        if line == "":
            for key, value in models.storage.all().items():
                string = str(value)
                list_all.append(string)
            print(list_all)
        elif list_line[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == list_line[0]:
                    string = str(value)
                    list_all.append(string)
            print(list_all)

    def update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attrubute (save the change into the JSON file)
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()