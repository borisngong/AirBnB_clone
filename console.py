import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for interacting with a file storage system.
    """

    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel}
    __storage = FileStorage()

    def do_create(self, line):
        """
        Creates a new instance of a class specified by the user.

        Usage: create <class_name>
        """
        self.__storage.reload()  # Reload storage before creating a new instance
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Displays the string representation of an instance specified by the class name and instance ID.

        Usage: show <class_name> <instance_id>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        print(self.__storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance specified by the class name and instance ID.

        Usage: destroy <class_name> <instance_id>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in self.__storage.all():
            print("** no instance found **")
            return
        del self.__storage.all()[key]
        self.__storage.save()

    def do_all(self, line):
        """
        Displays the string representation of all instances or instances of a specific class.

        Usage: all [class_name]
        """
        args = shlex.split(line)
        if len(args) == 0:
            print([str(obj) for obj in self.__storage.all().values()])
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in self.__storage.all().items() if key.startswith(class_name + '.')])

    def do_update(self, line):
        """
        Updates the attributes of an instance specified by the class name, instance ID, attribute name, and new attribute value.

        Usage: update <class_name> <instance_id> <attribute_name> <attribute_value>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
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
        except ValueError:
            print("Attribute value must be of type {}".format(attr_type.__name__))
            
    def do_EOF(self, user_input):
        """
        Command responsible for exiting the program elegantly when the user enters 'EOF' (Ctrl+D).
        """
        print()
        return True
    
    def help_EOF(self):
        """
        Provide help information for the 'EOF' command.
        """
        print("Command to exit the program elegantly 'EOF' (Ctrl+D)")

    def do_quit(self, user_input):
        """
        Exit the program when the user enters 'quit'.
        """
        return True
    
    def help_quit(self):
        """
        Provide help information for the 'quit' command.
        """
        print("Quit command to exit the program")
    
    def emptyline(self):
        """
        Called when an empty line is entered in the prompt.
        """
        pass
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()