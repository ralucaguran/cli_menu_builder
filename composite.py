import sys
import importlib

class Component(object):
    def do(self):
        pass

    def print_children(self, indent=''):
        print '{0}{1}'.format(indent, self.text)
        indent += '  '
        for child in self._children:
            child.print_children(indent)

class Composite(Component):
    def __init__(self, text=''):
        self.text = text
        self.action_handler = None
        self._children = []

    def __str__(self):
        return self.text

    def add(self, child):
        self._children.append(child)

    def get_child(self, path):
        child = self
        for ch in str(path):
            child = child._children[int(ch)-1]
        return child

class Leaf(Component):
    def __init__(self, text, action_handler, actions_module):
        self.text = text
        self.action_handler = action_handler
        self.actions_module = actions_module

    def __str__(self):
        return self.text

    def do(self):
        getattr(self.actions_module, self.action_handler)()

    def print_children(self, indent=''):
        print '{0}{1}'.format(indent, self.text)

