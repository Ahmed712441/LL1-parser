from GUI.tree import TreeNodeDrawing
from GUI.settings import EPSILON

class plusTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        
        super().__init__(treecanvas,level,parent,left, right, None,'+', True)
    
    # def __str__(self) :
    #     return '+'

class minusTerminal(TreeNodeDrawing):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'-', True)
    
    # def __str__(self) :
    #     return '-'

class leftBracketTerminal(TreeNodeDrawing):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'(', True)

    # def __str__(self) :
    #     return '('

class rightBracketTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,')', True)
    
    # def __str__(self) :
    #     return ')'

class multiplyTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'*', True)

    # def __str__(self) :
    #     return '*'

class divisionTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'/', True)
    
    # def __str__(self) :
    #     return '/'

class EpsilonTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,EPSILON, True)
    
    # def __str__(self) :
    #     return EPSILON

class dollarTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'$', True)
    
    # def __str__(self) :
    #     return '$'

class IDTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'ID', True)
    
    def __repr__(self) -> str:
        return 'ID'

class NumTerminal(TreeNodeDrawing):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'Num', True)
    
    def __repr__(self) -> str:
        return 'Num'