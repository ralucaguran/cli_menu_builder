#!/usr/bin/python

import json
import sys
from composite import *
import importlib

def build_menu_from_dict(dictionary, menu, actions_module):
    for k,v in dictionary.items():
        if isinstance(v, dict):
            composite = Composite(k)
            menu.add(composite)
            build_menu_from_dict(v,composite,actions_module)
        else:
            menu.add(Leaf(k,v,actions_module))

def print_usage_and_exit():
    print 'Usage: {0} <json menu> <handlers module>\n'\
            'e.g. {0} example/animals.json example.animals_handlers'.format(sys.argv[0])
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print_usage_and_exit()

    in_json = sys.argv[1]
    try:
        with open(in_json,'r') as json_file:
            animals_dict = json.load(json_file)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit(1)

    actions_module = importlib.import_module(sys.argv[2])
    menu = Composite()
    build_menu_from_dict(animals_dict, menu, actions_module)
    while True:
        menu.print_children()
        try:
            choice = input('Select choice:')
        except SyntaxError as e:
            sys.exit(0)
        menu.get_child(choice).do()

if __name__=="__main__":
    main()

