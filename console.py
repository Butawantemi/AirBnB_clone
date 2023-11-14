#!/usr/bin/python3

import cmd
import models
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb) "
    clslist = ["BaseModel","User", "Amenity", "City", "Place", "Review", "State"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True
        
    def do_help(self, args):
        """help"""
        cmd.Cmd.do_help(self, args)

        
    def do_show(self, arg):
        """Show instance based on id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clsDict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            instance = args[0] + '.' + args[1]
            if instance in obj.keys():
                print(obj[instance])
            else:
                print("** no instance found **")
                
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        my_list = args.split()
        if not my_list:
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.allowed_obj:
            print("** class doesn't exist **")
        else:
            my_object = eval(my_list[0] + '()')

            for i in range(1, len(my_list)):
                res = my_list[i].split('=')
                res[1] = res[1].replace('_', ' ')
                setattr(my_object, res[0], res[1])

            my_object.save()
            print(my_object.id)
                
    def do_destroy(self, arg):
        """destroy instance based on id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clsDict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            instance = args[0] + '.' + args[1]
            if instance in objects.keys():
                del(objects[instance])
                models.storage.save()
            else:
                print("** no instance found **")
                
    def do_all(self, arg):
        """prints all instances based or not on the class name"""
        args = arg.split()
        if not arg or args[0] in HBNBCommand.clsDict:
            args = []
            objects = models.storage.all()
            for instance in objects.values():
                args.append(instance.__str__())
            print(args)
        else:
            print("** class doesn't exist **")
            
            
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clsDict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            objects = models.storage.all()
            instance = "{}.{}".format(args[0], args[1])
            if instance in objects.keys():
                for value in objects.values():
                    try:
                        attr_type = type(getattr(value, args[2]))
                        args[3] = attr_type(args[3])
                    except AttributeError:
                        pass
                setattr(value, args[2], args[3])
                models.storage.save()
            else:
                print("** no instance found **")

    
    def postloop(self):
        """print new line after each loop"""
        print()
    
    def emptyline(self):
        """empty line"""
        pass
                
                
if __name__ == '__main__':
    HBNBCommand().cmdloop()

