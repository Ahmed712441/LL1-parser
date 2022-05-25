from GUI.tree import TreeNode
from GUI.settings import EPSILON

class plusTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'+', True)
        self.pirority = 2

class minusTerminal(TreeNode):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'-', True)
        self.pirority = 2
    
class leftBracketTerminal(TreeNode):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'(', True)

    
class rightBracketTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,')', True)
    
    
class multiplyTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'*', True)
        self.pirority = 1
    
class divisionTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'/', True)
        self.pirority = 1
    
class EpsilonTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,EPSILON, True)
    
    
class dollarTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'$', True)
    
    
class IDTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'id', True)
        self.pirority = 0
    
    def __repr__(self) -> str:
        return 'id'

class NumTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'Num', True)
        self.pirority = 0

    def __repr__(self) -> str:
        return 'Num'