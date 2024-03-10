#!/usr/bin/python3
'''This module has a program that contains
the entry point of the command interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''This a class that creates an entry point for a command interpreter for
    my AirBnB project console

    Attributes:
        prompt (str): The prompt name for the console
    '''
    prompt = "(hbnb)"

    def do_quit(self, cmd_line):
        '''Handles exit or quit when the user enters the command quit'''
        return True

    def do_EOF(self, cmd_line):
        '''Handles the EOF smoothly'''
        return True

    def emptyline(self):
        '''Handles an emptyline plus + ENTER by not executing anything'''
        pass

    def help_quit(self):
        '''The help for quit command'''
        print("Quit command to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
