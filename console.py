#!/usr/bin/python3
'''building the console for command intepretation'''
import cmd
from models import storage
from models.base_model import BaseModel
classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

class HBNBCommand(cmd.Cmd):
    ''' the command line intepreter
    '''
    prompt = '(hbnb)'


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

    def do_show(self, inp):
        '''Prints the string representation of a
        n instance based on the class name and id'''
        stuffs = inp.split(' ')
        if len(inp) == 0:
            print("** class name missing **")
            return
        elif stuffs[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(stuffs) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = stuffs[0] + '.' + stuffs[1]
        for obj_id in all_objs.keys():
            if s == obj_id:
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** no instance found **")
        pass


    def do_quit(self, line):
       '''type quit and the program will close instantly'''
       return True

    def emptyline(self):
        """ Method called when an empty line is entered in response
        to the prompt."""
        pass
    def do_EOF(self, line):
        """ press Ctrl D - the program will exit cleanly"""
        print()
        return True
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

