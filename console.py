#!/usr/bin/python3
"""
An interface for command-line interaction with the application
is provided by this module.
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import shlex


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
    __available_classes = {"BaseModel": BaseModel}
    __storage = FileStorage()

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

    def do_create(self, user_input):
        """
       Establishes a new instance of the user-specified class.

        Usage: create <class_name>
        """
        self.__storage.reload()
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__available_classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__available_classes[target_class]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, user_input):
        """
        shows the instance's string representation that is determined
        by the instance ID and class name

        Usage: show <class_name> <instance_id>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__available_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = target_class + '.' + obj_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        print(self.__storage.all()[key])

    def do_destroy(self, user_input):
        """
        Removes the instance that is indicated by the instance ID
        and class name.

        Usage: destroy <class_name> <instance_id>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__available_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = target_class + '.' + obj_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        del self.__storage.all()[key]
        self.__storage.save()

    def do_all(self, user_input):
        """
        shows all instances or instances of a particular class string
        represention

        Usage: all [class_name]
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print([str(obj) for obj in self.__storage.all().values()])
            return
        target_class = args[0]
        if target_class not in self.__available_classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in self.__storage.all().items()
               if key.startswith(target_class + '.')])

    def do_update(self, user_input):
        """
        Responsible for updating an instance's attributes using the class
        name, instance ID, attribute name, and new attribute value as input.
        Usage:
        update <class_name> <instance_id> <attribute_name> <attribute_value>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__available_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = target_class + '.' + obj_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value_str = args[3]
        obj = self.__storage.all()[key]

        # Create the attribute if it doesn't exist
        if not hasattr(obj, attr_name):
            setattr(obj, attr_name, "")

        attr_type = type(getattr(obj, attr_name))
        try:
            attr_value = attr_type(attr_value_str)
            setattr(obj, attr_name, attr_value)
            self.__storage.save()
        except Exception:
            pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
