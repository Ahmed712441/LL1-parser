from GUI.tree import TreeNodeDrawing
from tkinter import *
from GUI.settings import *
from parser.terminals import *

class Rule:

    def __init__(self,rule_name,rules=None):
        self.__rule_name = rule_name
        self.__rule_dict = rules

    def __str__(self):
        return self.__rule_name

    def raise_exception(self,input):
        raise Exception(f'{self.__str__()} rule can\'t parse {input}')

    def propagate(self,input):
        
        id = self.check_identifier(input)
        num = self.check_int(input)
        str =  'id' if id else 'Num' if num else input
        children = self.__rule_dict[str]
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
                if not ( ( char >= '1' and char <= '9') or ( char >= 'a' and char <= 'z') or ( char >= 'A' and char <= 'Z')):
                    return False
        return True

    @staticmethod
    def check_int(input):
        try:
            int(input[0])
            return True
        except:
            return False




class Exp(TreeNodeDrawing,Rule):
    
    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['('] = [ Term ,ExpDash ]
        rules['id'] = [ Term ,ExpDash ]
        rules['Num'] = [ Term ,ExpDash ] 
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Exp', False)
        Rule.__init__(self,rule_name= 'Exp',rules=rules)


class ExpDash(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['+'] = [Addop,Term,ExpDash] 
        rules['-'] = [Addop,Term,ExpDash]
        rules[')'] = [EpsilonTerminal]
        rules['$'] = [EpsilonTerminal] 
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Exp\'', False)
        Rule.__init__(self,rule_name= 'Exp\'',rules=rules)


class Addop(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['+'] = [plusTerminal] 
        rules['-'] = [minusTerminal]
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Addop', False)
        Rule.__init__( self,rule_name= 'Addop',rules=rules)
        

class Mullop(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['*'] = [multiplyTerminal] 
        rules['/'] = [divisionTerminal]
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Mullop', False)
        Rule.__init__( self,rule_name= 'Mullop',rules=rules)


class Factor(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['id'] = [IDTerminal] 
        rules['Num'] = [NumTerminal]
        rules['('] = [leftBracketTerminal,Exp,rightBracketTerminal]
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Factor', False)
        Rule.__init__(self, rule_name='Factor',rules=rules)

    
class Term(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['id'] = [Factor,TermDash] 
        rules['Num'] = [Factor,TermDash]
        rules['('] = [Factor,TermDash]
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Term', False)
        Rule.__init__( self,rule_name='Term',rules=rules)
        

        

class TermDash(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        rules = dict()
        rules['*'] = [Mullop,Factor,TermDash]
        rules['/'] = [Mullop,Factor,TermDash]
        rules['+'] = [EpsilonTerminal]
        rules['-'] = [EpsilonTerminal]
        rules[')'] = [EpsilonTerminal]
        rules['$'] = [EpsilonTerminal]
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Term\'', False)
        Rule.__init__( self,rule_name='Term\'',rules=rules)

    

    