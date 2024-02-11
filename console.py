#!/usr/bin/python3
"""
An interface for command-line interaction with the application
is provided by this module.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
   The program can be interfaced with through the command-line interface
   provided by the HBNBCommand class
    """

    prompt = "(hbnb) "
    """
    Represents the string the user sees while using the command-line
    interface
    """
    def emptyline(self):
        """
        On an empty line, take no action
        """
        pass

    def do_EOF(self, user_input):
        """
        Command in charge of safely ending the program when the
        user types 'EOF' (Ctrl+D).
        """
        print("")
        return True

    def help_EOF(self):
        """
        Provide help information for the 'EOF' command.
        """
        print("Command to exit the program elegantly 'EOF' (Ctrl+D)")

    def do_quit(self, user_input):
        """
        When the user types "quit," the program will exit.
        """
        return True

    def help_quit(self):
        """
        Provide helpful information for the 'quit' command.
        """
        print("Quit command to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
