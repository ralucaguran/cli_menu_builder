import sys
import importlib

class Component(object):
    def __init__(self, text=''):
        self.text = text

    def __str__(self):
        return self.text
 
    def do(self):
        pass

    def show(self, num_indents=-1):
        print '{0}{1}'.format(num_indents*'  ', self)

class Composite(Component):
    def __init__(self, text=''):
        super(Composite,self).__init__(text)
        self._children = []

    def add(self, child):
        self._children.append(child)

    def get_child(self, path):
        child = self
        for ch in str(path):
            child = child._children[int(ch)-1]
        return child

    def show(self, num_indents=-1):
        super(Composite,self).show(num_indents)
        for child in self._children:
            child.show(num_indents+1)

class Leaf(Component):
    def __init__(self, text, action_handler, actions_module):
        super(Leaf,self).__init__(text)
        self.action_handler = action_handler
        self.actions_module = actions_module

    def do(self):
        getattr(self.actions_module, self.action_handler)()


