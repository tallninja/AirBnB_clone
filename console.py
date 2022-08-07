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
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
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
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in objects.keys():
            print("** no instance found **")
        else:
            print(objects[f"{arg[0]}.{arg[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        objects = storage.all()
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in objects.keys():
            print("** no instance found **")
        else:
            del objects[f"{arg[0]}.{arg[1]}"]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        objects = storage.all()
        objects_list = []
        for k, v in objects.items():
            objects_list.append(str(v))
        print(str(objects_list))
        if arg and arg not in classes.keys():
            print("** class doesn't exist ** ")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        objects = storage.all()
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in objects.keys():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            for v in objects.values():
                try:
                    atribute = type(getattr(v, arg[2]))
                    arg[3] = atribute(arg[3])
                except AttributeError:
                    pass
                setattr(v, arg[2], arg[3].strip('"'))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
