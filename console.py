#!/usr/bin/python3
"""
Module for working with Class HBNBCommand 
"""

import cmd
import shlex
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for interacting with a file storage system.
    """

    prompt = '(hbnb) '

    __storage = FileStorage()
    __classes = {
        "BaseModel": BaseModel,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
        "User": User
    }

    def emptyline(self):
        """
        Called when an empty line is entered in the prompt.
        """
        pass

    def do_EOF(self, user_input):
        """
        Command responsible for exiting the program elegantly when
        the user enters 'EOF' (Ctrl+D).
        """
        print()
        return True

    def do_quit(self, user_input):
        """
        Exit the program when the user enters 'quit'.
        """
        return True

    def help_quit(self):
        """
        Help information for the 'quit' command.
        """
        print("Quit command to exit the program")

    def do_create(self, user_input):
        """
        Creates a new instance of a class specified by the user.

        Usage: create <class_name>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[target_class]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, user_input):
        """
        shows the instance's string representation, which is determined by
        the instance ID and class name.

        Usage: show <class_name> <instance_id>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = target_class + '.' + instance_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        print(self.__storage.all()[key])

    def do_destroy(self, user_input):
        """
        Removes an instance that has the class name and instance ID supplied.

        Usage: destroy <class_name> <instance_id>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = target_class + '.' + instance_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        del self.__storage.all()[key]
        self.__storage.save()

    def do_all(self, user_input):
        """
        displays all instances or all instances of
        a specific class as strings.

        Usage: all [class_name]
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print([str(obj) for obj in self.__storage.all().values()])
            return
        target_class = args[0]
        if target_class not in self.__classes:
            print("** class doesn't exist **")
            return
        filtered_instances = []
        for key, obj in self.__storage.all().items():
            if key.startswith(target_class + '.'):
                filtered_instances.append(str(obj))
        print(filtered_instances)

    def update_instance_from_dict(self, target_class, instance_id, serialized_dict):
        """
        Update an instance with attribute values provided in a serialized
        dictionary.

        Args:
        target_class (str): The name of the target class.
        instance_id (str): The ID of the instance to update.
        serialized_dict (str): serialized dictionary (attribute-value pairs)
        """
        serialized_json = serialized_dict.replace("'", '"')
        attributes_dict = json.loads(serialized_json)

        if not target_class:
            print("** class name missing **")
        elif target_class not in self.__classes:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(target_class, instance_id)
            if instance_key not in self.__storage.all():
                print("** no instance found **")
            else:
                instance_obj = self.__storage.all()[instance_key]
                for attribute, value in attributes_dict.items():
                    if attribute not in ['id', 'created_at', 'updated_at']:
                        setattr(instance_obj, attribute, value)

            instance_obj.save()


    def do_update(self, user_input):
        """
        Responsible for Updating an instance specified by the class name
        and instance ID by adding or updating attribute values.

        Usage: update <class_name> <instance_id> <dictionary_representation>
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_val_pairs = args[2]
        updated_value = args[3]
        if attr_val_pairs in ['id', 'created_at', 'updated_at']:
            return
        key = target_class + '.' + instance_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        if attr_val_pairs.startswith("{"):
            self.update_instance_from_dict(target_class, instance_id, attr_val_pairs)
            return
        setattr(self.__storage.all()[key], attr_val_pairs, updated_value)
        self.__storage.all()[key].save()

    def default(self, user_input):
        """
        It is called when the command entered by the user is not recognized.

        Syntax for advanced commands:
        <class_name>.all()
        <class_name>.count()
        <class_name>.show(<instance_id>)
        <class_name>.destroy(<instance_id>)
        <class_name>.update(<instance_id>, <attribute_name>, "<attribute_value>")
        <class_name>.update(<instance_id>, <dictionary_representation>)
        """
        c_instructions = {
            "all": self.do_all,
            "count": self.count_instances,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        if '.' in user_input:
            target_class = user_input.split('.')[0]
            if target_class in self.__classes:
                instruction = user_input.split('.')[1].split('(')[0]
                if instruction in c_instructions:
                    instance_id = user_input.split('(')[1].split(')')[0].replace('"', '')
                    if instruction == "update":
                        if '{' in user_input:
                            serialized_dict = user_input.split('(')[1].split(')')[0].split(',', 1)[1].strip()
                            self.update_instance_from_dict(target_class, instance_id, serialized_dict)
                        else:
                            attribute_name, attribute_value = (
                                user_input.split('(')[1].split(')')[0].split(',', 1)
                            )
                            attribute_name = attribute_name.strip()
                            attribute_value = attribute_value.strip()[1:-1]
                            update_args = f"{target_class} {instance_id} {attribute_name} {attribute_value}"
                            self.do_update(update_args)
                    else:
                        show_args = f"{target_class} {instance_id}"
                        c_instructions[instruction](show_args)
                        return
        print("*** Unknown syntax: {}".format(user_input))


    def count_instances(self, user_input):
        """
        Responsible for counting the number of instances of a specific class

        Usage: <class_name>.count()
        """
        args = shlex.split(user_input)
        if len(args) == 0:
            print("** class name missing **")
            return
        target_class = args[0]
        if target_class not in self.__classes:
            print("** class doesn't exist **")
            return
        aggregate = 0
        for key in self.__storage.all():
            if key.split('.')[0] == target_class:
                aggregate += 1
        print(aggregate)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
