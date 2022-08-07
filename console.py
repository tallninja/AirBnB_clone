#!/usr/bin/python3

import cmd
from models.classes import classes
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
        if arg in [k for k in classes.keys()]:
            new_model = classes[arg]()
            new_model.save()
            print(new_model.id)
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
