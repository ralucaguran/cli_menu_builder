import sys

class Component(object):
    def __init__(self, text=''):
        self.text = text

    def __str__(self):
        return self.text
 
    def do(self):
        pass

    def show(self, idx=0, num_indents=-1):
        print '{}{}.{}'.format(num_indents*'  ', idx, self) if idx != 0 else ''

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

    def show(self, idx=0, num_indents=-1):
        super(Composite,self).show(idx,num_indents)
        for pos in range(len(self._children)):
            self._children[pos].show(pos+1,num_indents+1)

class Leaf(Component):
    def __init__(self, text, action_handler, actions_module):
        super(Leaf,self).__init__(text)
        self.action_handler = action_handler
        self.actions_module = actions_module

    def do(self):
        getattr(self.actions_module, self.action_handler)()

