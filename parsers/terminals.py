from GUI.tree import TreeNode
from GUI.settings import EPSILON

class plusTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        
        super().__init__(treecanvas,level,parent,left, right, None,'+', True)
    

class minusTerminal(TreeNode):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'-', True)
    
    
class leftBracketTerminal(TreeNode):
    def __init__(self,treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'(', True)

    
class rightBracketTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,')', True)
    
    
class multiplyTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'*', True)

    
class divisionTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'/', True)
    
    
class EpsilonTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,EPSILON, True)
    
    
class dollarTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'$', True)
    
    
class IDTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'ID', True)
    
    def __repr__(self) -> str:
        return 'ID'

class NumTerminal(TreeNode):
    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__(treecanvas,level,parent,left, right, None,'Num', True)
    
    def __repr__(self) -> str:
        return 'Num'