from GUI.tree import TreeNode
from tkinter import *
from GUI.settings import *
from parsers.terminals import *

class Rule:

    def __init__(self,rule_name,rules=None):
        self.__rule_name = rule_name
        self.rule_dict = rules

    def __str__(self):
        return self.__rule_name

    def raise_exception(self,input):
        raise Exception(f'{self.__str__()} rule can\'t parse {input}')

    def propagate(self,input):
        
        id = self.check_identifier(input)
        num = self.check_int(input)
        str =  'id' if id else 'Num' if num else input
        try:
            children = self.rule_dict[str]
        except:
           self.raise_exception(input)
        self.add_children(children)
        children = self.get_children()
        if (isinstance(children[0],(NumTerminal,IDTerminal))):
            children[0].set_label(input)
        return children
        
    
    @staticmethod
    def check_identifier(input):
        try:
            int(input[0])
            return False
        except:
            for char in input:
                if not ( ( char >= '0' and char <= '9') or ( char >= 'a' and char <= 'z') or ( char >= 'A' and char <= 'Z')):
                    return False
        return True

    @staticmethod
    def check_int(input):
        try:
            int(input[0])
            return True
        except:
            return False




class Exp(TreeNode,Rule):
    
    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['('] = [ Term ,ExpDash ]
        rules['id'] = [ Term ,ExpDash ]
        rules['Num'] = [ Term ,ExpDash ] 
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Exp', False)
        Rule.__init__(self,rule_name= 'Exp',rules=rules)


class ExpDash(TreeNode,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['+'] = [Addop,Term,ExpDash] 
        rules['-'] = [Addop,Term,ExpDash]
        rules[')'] = [EpsilonTerminal]
        rules['$'] = [EpsilonTerminal] 
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Exp\'', False)
        Rule.__init__(self,rule_name= 'Exp\'',rules=rules)


class Addop(TreeNode,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['+'] = [plusTerminal] 
        rules['-'] = [minusTerminal]
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Addop', False)
        Rule.__init__( self,rule_name= 'Addop',rules=rules)
        

class Mullop(TreeNode,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['*'] = [multiplyTerminal] 
        rules['/'] = [divisionTerminal]
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Mullop', False)
        Rule.__init__( self,rule_name= 'Mullop',rules=rules)


class Factor(TreeNode,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['id'] = [IDTerminal] 
        rules['Num'] = [NumTerminal]
        rules['('] = [leftBracketTerminal,Exp,rightBracketTerminal]
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Factor', False)
        Rule.__init__(self, rule_name='Factor',rules=rules)

    
class Term(TreeNode,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['id'] = [Factor,TermDash] 
        rules['Num'] = [Factor,TermDash]
        rules['('] = [Factor,TermDash]
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Term', False)
        Rule.__init__( self,rule_name='Term',rules=rules)
        

        

class TermDash(TreeNode,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['*'] = [Mullop,Factor,TermDash]
        rules['/'] = [Mullop,Factor,TermDash]
        rules['+'] = [EpsilonTerminal]
        rules['-'] = [EpsilonTerminal]
        rules[')'] = [EpsilonTerminal]
        rules['$'] = [EpsilonTerminal]
        TreeNode.__init__(self,treecanvas,level,parent,left, right, None,'Term\'', False)
        Rule.__init__( self,rule_name='Term\'',rules=rules)

    

    