#!/usr/bin/python3
'''This module has a program that contains
the entry point of the command interpreter'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''This a class that creates an entry point for a command interpreter for
    my AirBnB project console

    Attributes:
        prompt (str): The prompt name for the console
    '''
    prompt = "(hbnb)"

    def do_create(self, cmd_line):
        '''create: Creates a new instance of BaseModel
        and saves it (to the JSON file) and prints the id

        Args:
            cmd_line (str): The input command
        '''
        args = cmd_line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        try:
            class_obj = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        new_obj = class_obj()
        new_obj.save()
        print("{}".format(new_obj.id))

    def do_show(self, cmd_line):
        ''' Prints the string representation of an instance based on
        class name and id.

        Args:
            cmd_line (str): The input command
        '''
        args = cmd_line.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]

        search_obj = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if search_obj in all_objs:
            obj = all_objs[search_obj]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, cmd_line):
        '''Deletes an instance based on the class name and id
        and (save the changes into the JSON file).

        Args:
            cmd_line (str): The input command
        '''
        args = cmd_line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        search_obj = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if search_obj in all_objs:
            del(all_objs[search_obj])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, cmd_line):
        '''Prints all string representation of all instances based
        or not on the class name.

        Args:
            cmd_line (str): The input command
        '''
        args = cmd_line.split()
        objs_filtered = {}
        if len(args) == 1:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            all_objs = storage.all()
            for key, obj in all_objs.items():
                if key.startswith(class_name):
                    objs_filtered[key] = obj
        elif len(args) == 0:
            objs_filtered = storage.all()

        obj_string = [str(obj) for obj in objs_filtered.values()]

        print(obj_string)

    def do_update(self, cmd_line):
        '''updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Args:
            cmd_line (str): The input command
        '''
        args = cmd_line.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        all_objs = storage.all()

        search_obj = "{}.{}".format(class_name, obj_id)

        if search_obj not in all_objs:
            print("** no instance found **")
            return

        upd_obj = all_objs[search_obj]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        upd_att = args[2]
        upd_val = args[3]

        if upd_att in ["id", "created_at", "updated_at"]:
            print("** You cannot update {} attribute **".format(upd_att))
            return

        if hasattr(upd_obj, upd_att):
            existing_att = getattr(upd_obj, upd_att)
            if isinstance(existing_att, str) and\
                    (upd_val.startswith('"') and upd_val.endswith('"')):
                upd_val = upd_val.strip('"')
                setattr(
                        upd_obj, upd_att,
                        type(getattr(upd_obj, upd_att))(upd_val)
                        )
                storage.save()
                return
            elif isinstance(existing_att, int) and\
                    (not upd_val.startswith('"') and
                        not upd_val.endswith('"')):
                setattr(
                        upd_obj, upd_att,
                        type(getattr(upd_obj, upd_att))(upd_val)
                        )
                storage.save()
                return
            elif isinstance(existing_att, float) and\
                    (not upd_val.startswith('"') and
                        not upd_val.endswith('"')):
                setattr(
                        upd_obj, upd_att,
                        type(getattr(upd_obj, upd_att))(upd_val)
                        )
                storage.save()
                return
            else:
                if isinstance(existing_att, str):
                    print(
                        f"TypeError({upd_att} must be a string in \"\" quotes)"
                        )
                elif isinstance(existing_att, int):
                    print(f"TypeError({upd_att} must be an integer value)")
                elif isinstance(existing_att, float):
                    print(
                        f"TypeError({upd_att} must be an float/decimal value)"
                        )

        else:
            if upd_val.startswith('"') and upd_val.endswith('"'):
                setattr(upd_obj, upd_att, upd_val.strip('"'))
            else:
                try:
                    num_val = int(upd_val)
                except ValueError:
                    try:
                        num_val = float(upd_val)
                    except ValueError:
                        print("The value must be a string, integer or float")
                        return

                setattr(upd_obj, upd_att, num_val)
                storage.save()

    def do_quit(self, cmd_line):
        '''Handles exit or quit when the user enters the command quit'''
        return True

    def do_EOF(self, cmd_line):
        '''Handles the EOF smoothly'''
        return True

    def emptyline(self):
        '''Handles an emptyline plus + ENTER by not executing anything'''
        pass

    def help_create(self):
        '''help coomand for create'''
        print("Creates a new instance of BaseModel")
        print("saves it (to the JSON file) and prints the id\n")
        print("Example:\n$ create BaseModel")

    def help_show(self):
        '''Help command for show'''
        print("Prints the string representation of an instance based on")
        print("the class name and id\n")
        print("Example:\n$ show BaseModel 1234-1234-1234")

    def help_destroy(self):
        '''Help command for destroy'''
        print("Deletes an instance based on the class name and id")
        print("and (save the change into the JSON file)\n")
        print("Example:\n$ destroy BaseModel 1234-1234-1234")

    def help_all(self):
        '''Help command for all'''
        print("Prints all string representation of all instances")
        print("based or not on the class name.\n")
        print("Example:\n$ all BaseModel\nor\n$ all")

    def help_update(self):
        '''Help command for update'''
        print("Updates an instance based on the class name and id by adding")
        print("or updating attribute (save the changes into the JSON file).\n")
        print("Example:")
        print("$ update BaseModel 1234-1234-1234 email \"aibnb@mail.com\"")

    def help_quit(self):
        '''The help for quit command'''
        print("Quit command to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
