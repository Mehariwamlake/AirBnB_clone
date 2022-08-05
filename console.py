#!/usr/bin/python3
"""
Module for the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.json_helpers import save_to_json_file

save_to_json = save_to_json_file.save_to_json_file 
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

    def do_create(self, class_name):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in classes:
            print("** class doesn't exist **")
        else:
            new_obj = classes[class_name]()
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

    def do_destroy(self, id_str):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
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
            if key in all_objs:
                del all_objs[key]
                dics = {k: v.to_dict() for k, v in all_objs.items()}
                save_to_json(dics, "file.json")
                storage.reload()
            else:
                print("** no instance found **")

    def do_all(self, class_name):
        """
        Prints all string representation of all instances
        based or not on the class name. 
        Ex: $ all BaseModel or $ all
        """
        objs = storage.all()
        if not class_name:
            obj_arr = [str(v) for k, v in objs.items()]
            print(obj_arr)
        elif class_name not in classes:
            print("** class doesn't exist **")
        else:
            obj_arr = [str(v) for k, v in objs.items() 
             if v.__class__.__name__ == class_name]
            print(obj_arr)

    def do_update(self, id_str):
        """

        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
