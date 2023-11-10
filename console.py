#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime
from shlex import shlex

class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '
    clsDict = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        return True
        
    def do_show(self, arg):
        """Prints the string representation of an instance and id"""
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
                
    def do_destroy(self, arg):
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


    def emptyline(self):
        '''empty line
        '''
        pass
                
                
if __name__ == '__main__':
    HBNBCommand().cmdloop()

