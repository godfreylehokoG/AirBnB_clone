#!/usr/bin/python3

import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):

        return False

    def do_quit(self, arg):

        return True

    def do_EOF(self, arg):

        return True

    def postloop(self):

        print()

    def do_create(self, arg):
        arg = [s for s in arg.split()]
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.storage.all_models.keys():
            print("** class doesn't exist **")
        else:
            bm = self.storage.all_models.get(arg[0])()
            bm.save()
            print(bm.to_dict().get("id"))
