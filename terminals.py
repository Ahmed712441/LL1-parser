from .treenode import TreeNodeDrawing
from .settings import EPSILON

class plusTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, '+')
    
    def __str__(self) :
        return '+'

class minusTerminal(TreeNodeDrawing):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, '-')
    
    def __str__(self) :
        return '-'

class leftBracketTerminal(TreeNodeDrawing):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, '(')

    def __str__(self) :
        return '('

class rightBracketTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, ')')
    
    def __str__(self) :
        return ')'

class multiplyTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, '*')

    def __str__(self) :
        return '*'

class divisionTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, '/')
    
    def __str__(self) :
        return '/'

class EpsilonTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, EPSILON)
    
    def __str__(self) :
        return EPSILON

class dollarTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, '$')
    
    def __str__(self) :
        return '$'

class IDTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, 'ID')
    
    def __str__(self) :
        return 'ID'

class NumTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(True, treecanvas, level, parent, left, right, 'Num')
    
    def __str__(self) :
        return 'Num'