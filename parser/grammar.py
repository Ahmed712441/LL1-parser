from abc import abstractclassmethod
from GUI.tree import TreeNodeDrawing
from tkinter import *
from GUI.settings import *
from parser.terminals import *

class Rule:

    def __init__(self,rule_name):
        self.__rule_name = rule_name

    def __str__(self):
        return self.__rule_name

    def raise_exception(self,input):
        raise Exception(f'{self.__str__()} rule can\'t parse {input}')

    @abstractclassmethod
    def propagate(self,input):
        pass
    
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
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Exp', False)
        Rule.__init__(self,rule_name= 'Exp')


    def propagate(self,input):
        children = [] 
        if input == '(' or  Rule.check_identifier(input) or Rule.check_int(input) :
            children = [ Term ,ExpDash ]
            super().add_children(children)
            children = super().get_children()
        else:
            self.raise_exception(input)


        return children

class ExpDash(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Exp\'', False)
        Rule.__init__(self,rule_name= 'Exp\'')


    def propagate(self,input):
        children = []
        if input == '+' or input=='-':
            children = [Addop,Term,ExpDash]   
        elif input ==')'or input =='$' :
            children = [EpsilonTerminal]
        else:
            self.raise_exception(input)

        if children:
            super().add_children(children)
            children = super().get_children()


        return children

class Addop(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Addop', False)
        Rule.__init__( self,rule_name= 'Addop')
        
    def propagate(self,input):
        children = []
        if input == '+':
            children = [plusTerminal]
        elif input=='-':
            children = [minusTerminal]
        else:
            self.raise_exception(input)

        if children:
            super().add_children(children)
            children = super().get_children()

        return children

class Mullop(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Mullop', False)
        Rule.__init__( self,rule_name= 'Mullop')

    def propagate(self,input):
        children = []
        if input == '*':
            children = [multiplyTerminal]
        elif input=='/':
            children = [divisionTerminal]
        else:
            self.raise_exception(input)

        if children:
            super().add_children(children)
            children = super().get_children()


        return children

class Factor(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Factor', False)
        Rule.__init__(self, rule_name='Factor')

    def propagate(self,input):
        children = []
        reset_label = False
        if  Rule.check_identifier(input):
            children = [IDTerminal]
            reset_label = True
        elif Rule.check_int(input):
            children = [NumTerminal]
            reset_label = True
        elif input=='(':
            children = [leftBracketTerminal,Exp,rightBracketTerminal]
        else:
            self.raise_exception(input)

        if children:
            super().add_children(children)
            children = super().get_children()
            if reset_label:
                children[0].set_label(input)


        return children

class Term(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Term', False)
        Rule.__init__( self,rule_name='Term')
        

    def propagate(self,input):
        children = []
        if input =='(' or  Rule.check_identifier(input) or Rule.check_int(input) :
            children = [Factor,TermDash]
        else:
            self.raise_exception(input)

        if children:
            super().add_children(children)
            children = super().get_children()


        return children
        

class TermDash(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        TreeNodeDrawing.__init__(self,treecanvas,level,parent,left, right, None,'Term\'', False)
        Rule.__init__( self,rule_name='Term\'')

    def propagate(self,input):
        children = []
        if input =='*' or input == '/':
            children = [Mullop,Factor,TermDash]
        elif input =='+' or input =='-' or input ==')' or input=='$':
            children = [EpsilonTerminal]
        else:
            self.raise_exception(input)

        if children:
            super().add_children(children)
            children = super().get_children()
        
        return children


    