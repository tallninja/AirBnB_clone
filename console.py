#!/usr/bin/python3

import cmd

"""
console.py - entry point of the command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
    command line program
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """called when an empty line is entered in response to the prompt"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
