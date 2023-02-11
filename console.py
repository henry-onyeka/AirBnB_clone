#!/bin/usr/python3
'''building the console for command intepretation'''
import cmd
from cmd import Cmd

class HBNBCommand(cmd.Cmd):
    ''' the command line intepreter
    '''''
    prompt = '(hbnb)'


    def do_quit(self):
       '''type quit and the program will close instantly'''
       '''type quit and the program will close instantly'''
       return True

    def do_EOF(self, line):
        """ press Ctrl D - the program will exit cleanly"""
        print()
        return True
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

