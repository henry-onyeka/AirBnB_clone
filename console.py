#!/usr/bin/python3
'''building the console for command intepretation'''
import cmd

class HBNBCommand(cmd.Cmd):
    ''' the command line intepreter
    '''''
    prompt = '(AirBnB)'

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

    def do_quit(self, line):
       '''type quit and the program will close instantly'''
       return True

    def do_EOF(self, line):
        """ press Ctrl D - the program will exit cleanly"""
        print()
        return True
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

