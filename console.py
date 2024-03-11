#!/usr/bin/python3
'''This module has a program that contains
the entry point of the command interpreter'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''This a class that creates an entry point for a command interpreter for
    my AirBnB project console

    Attributes:
        prompt (str): The prompt name for the console
    '''
    prompt = "(hbnb)"

    def do_create(self, cmd_line):
        class_name = cmd_line.split()
        if not cmd_line:
            print("** class name missing **")

        try:
            class_obj = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")

        new_obj = class_obj()
        new_obj.save()
        print("{}".format(new_obj.id))

    def do_show(self, cmd_line):
        args = cmd_line.split()
        class_name = args[0]
        if len(args) == 0:
            print("** class name missing **")

        try:
            class_obj = globals()[class_name]
        except:
            print("** class doesn't exist **")

        if len(args) == 1:
            print("** instance id missing **")

        search_obj = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        found_obj = False
        
        for obj_key in all_objs.keys():
            if search_obj == obj_key:
                obj = all_objs[obj_key]
                print(obj)
                found_obj = True
                break
            
        if not found_obj:
            print("** no instance found **")
            
    def do_destroy(self, cmd_line):
        args = cmd_line.split()
        class_name = args[0]
        if len(args) == 0:
            print("** class name missing **")
        
        try:
            class_obj = globals()[class_name]
        except:
            print("** class doesn't exist **")

        if len(args) == 1:
            print("** instance id missing **")

        search_obj = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        found_obj = False

        for obj_key in all_objs.keys():
            if search_obj == obj_key:
                del(all_objs[obj_key])
                storage.save()
                break

        if not found_obj:
            print("** no instance found **")

    def do_all(self, cmd_line):
        args = cmd_line.split()
        args[0] = class_name
        try:
            class_obj = globals()[class_name]
        except:
            print("** class doesn't exist **")

        all_objs = storage.all()
        for obj_key in all_objs.keys():
            obj = all_objs[obj_key]
            print(obj)

            
    def do_update(self, cmd_line):
        args = cmd_line.split()
        all_objs = storage.all()
        search_obj = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        upd_obj = None
        found_object = False
        for obj_key in all_objs.keys():
            if search_obj == obj_key:
                upd_obj = all_objects[obj_key]
                found_obj = True
                break

        if len(args) == 0:
            print("** class name missing **")

        try:
            class_obj = globals()[class_name]
        except:
            print("** class doesn't exist **")

        if len(args) == 1:
            print("** instance id missing **")
        elif not found_obj:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        
        upd_att = args[2]
        upd_val = arg[3]
        for key, value in upd_obj.items():
            if upd_obj[upd_att] == "id":
                print("** You cannot update id attribute **")
            elif upd_obj[upd_att] == "created_at":
                print("** You cannot update created_at attribute **")
            elif upd_obj[upd_att] == "updated_at":
                print("** You cannot update updated_at attribute **")
            
            if upd_obj[key] == upd_att:
                k = upd_obj[key]
                if isinstance(k, int):


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
