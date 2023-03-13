#!/usr/bin/python3
"""This is a simple Console 'CMD'"""
import cmd


class HBNBCommand(cmd.Cmd):
    """prompt class """
    prompt = "(hbnb)"

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
