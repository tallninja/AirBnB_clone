#!/usr/bin/python3

import cmd
from models.classes import classes
from models import storage
from models.base_model import BaseModel

"""
console.py - entry point of the command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
    command line program
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """called when an empty line is entered in response to the prompt"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        else:
            new_model = classes[arg[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        objects = storage.all()
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif f"{arg[0]}.{arg[1]}" not in objects.keys():
            print("** no instance found **")
            return
        else:
            print(objects[f"{arg[0]}.{arg[1]}"])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
