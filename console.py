#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
    """Command processor"""

    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_count(self, cls_name):
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_create(self, type_model):
        """ Creates an instance according to a given class """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Shows string representation of an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True

=======
    """ the command interpreter of AirBnB project """

    prompt = '(hbnb) '

    def do_create(self, args):
        """ create a new instance of a class and prints the id """

        if len(args) == 0:
            print("** class name missing **")
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            for i in classes:
                if i == args:
                    a1 = str(args) + '()'
                    a = eval(a1)
            print(a.id)
            a.save()
        pass

    def do_show(self, args):
        """ Prints the json file of an instance of a class name and id """

        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = words[0] + '.' + words[1]
        for obj_id in all_objs.keys():
            if s == obj_id:
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** no instance found **")
        pass

    def do_all(self, args):
        """ Prints all string representation of all instances """

        if len(args) == 0:
            all_objs = storage.all()
            new_list = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                new_list.append("{}".format(obj))
            print(new_list)
        elif args not in classes:
            print("** class doesn't exist **")
        elif args in classes:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                key1 = obj_id.split('.')
                if key1[0] == args:
                    obj = all_objs[obj_id]
                    print("{}".format(obj))

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """

        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = words[0] + '.' + words[1]
        for key, value in all_objs.items():
            if s in key:
                del all_objs[str(s)]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        by adding or updating attribute """

        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        if len(words) == 3:
            print("** value missing **")
            return
        s1 = words[0] + '.' + words[1]
        all_objs = storage.all()
        for key, value in all_objs.items():
            if s1 in key:
                if len(words) == 2:
                    print("** attribute name missing **")
                    return
                if words[3][0] == "\"" and words[3][-1] == "\"":
                    setattr(value, words[2], words[3][1:-1])
                    storage.save()
                    return
                setattr(value, words[2], words[3])
                storage.save()
                return
        print("** no instance found **")

    def precmd(self, line):
        """
        """

        words = line.split('.', 1)
        if len(words) == 1:
            return cmd.Cmd.precmd(self, line)
        s1 = words[1][:-1].split('(', 1)
        t1 = s1[1].split(', ')
        if s1[1] == '':
            s = s1[0] + ' ' + words[0]
            return cmd.Cmd.precmd(self, s)
        if len(t1) >= 1:
            s = s1[0] + ' ' + words[0] + ' ' + t1[0][1:-1]
        if len(t1) >= 2:
            s = s + ' ' + t1[1][1:-1]
        if len(t1) >= 3:
            if t1[2][0] == "\"" and t1[2][-1] == "\"":
                t1[2] = t1[2][1:-1]
            s = s + ' ' + t1[2]
        return cmd.Cmd.precmd(self, s)

    def emptyline(self):
        """ Method called when an empty line is entered in response
        to the prompt."""

        pass

    def do_EOF(self, line):
        """ Ctrl D - the program will exit cleanly"""

        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """

        return True

>>>>>>> cd96624 (worked console)

if __name__ == '__main__':

    HBNBCommand().cmdloop()
