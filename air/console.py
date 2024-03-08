#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print("\nGoodbye!")
        return True

    def help_quit(self):
        """Display help message for the quit command."""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Display help message for the EOF command."""
        print("Exit the program on EOF")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass
         

if __name__ == '__main__':
    HBNBCommand().cmdloop()
