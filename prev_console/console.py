#!/usr/bin/python3
"""Inside the console module."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Inside the HBNBC class."""

    prompt = '(hbnb) '
    classes_str = ["BaseModel", "User",
                   "State", "City", "Place",
                   "Amenity", "Review"]
    classes = [BaseModel, User]

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print("")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")
        print("")

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            if line.strip() not in self.classes_str:
                print("** class doesn't exist **")
            else:
                print(eval(line)().id)
                storage.save()

    def help_create(self):
        print("Creates a new instance of BaseModel,"
              " saves it (to the JSON file) "
              "and prints the id")
        print("")

    def do_show(self, line):

        if not line:
            print("** class name missing **")
        elif line.strip().split()[0] not in self.classes_str:
            print("** class doesn't exist **")
        else:

            sline = line.split()
            dict_obj = storage.all()

            if len(sline) != 2:
                print("** instance id missing **")
            elif "{}.{}".format(sline[0], sline[1]) not in dict_obj:
                print("** no instance found **")
            else:
                print(dict_obj["{}.{}".format(sline[0], sline[1])])

    def help_show(self):
        print(" Prints the string representation"
              " of an instance based on the class name and id.")
        print("")

    def do_destroy(self, line):
        dict_obj = storage.all()
        sline = line.split()

        if not line:
            print("** class name missing **")
        elif line.strip().split()[0] not in self.classes_str:
            print("** class doesn't exist **")
        elif len(sline) != 2:
            print("** instance id missing **")
        elif "{}.{}".format(sline[0], sline[1]) not in dict_obj:
            print("** no instance found **")
        else:
            del dict_obj["{}.{}".format(sline[0], sline[1])]
            storage.save()

    def help_destroy(self):
        print(" Deletes an instance based on"
              " the class name and id (save the change into the JSON file)")
        print("")

    def do_all(self, line):

        if line.strip().split()[0] not in self.classes_str and line:
            print("** class doesn't exist **")
        else:
            dict_obj = storage.all()
            obj_list = []
            for one_obj in dict_obj.values():
                obj_list.append(str(one_obj))

            print(obj_list)

    def help_all(self):
        print("Prints all string representation of"
              " all instances based or not on the class name")

    def do_update(self, line):
        dict_obj = storage.all()
        sline = line.split()

        if not line:
            print("** class name missing **")
        elif line.strip().split()[0] not in self.classes_str:
            print("** class doesn't exist **")
        elif len(sline) == 1 and line.strip().split()[0] in self.classes_str:
            print("** instance id missing **")
        elif "{}.{}".format(sline[0], sline[1]) not in dict_obj:
            print("** no instance found **")
        elif len(sline) == 2:
            print("** attribute name missing **")
        elif len(sline) == 3:
            print("** value missing **")

        if len(sline) == 4:
            obj = dict_obj["{}.{}".format(sline[0], sline[1])]
            if sline[2] in obj.__class__.__dict__:
                obj.__dict__[sline[2]] = type(obj.__class__.__dict__[sline[2]])
            else:
                obj.__dict__[sline[2]] = sline[3]

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
