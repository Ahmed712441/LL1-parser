from abc import abstractclassmethod
from .treenode import TreeNodeDrawing
from tkinter import *
from .settings import *
from .terminals import *

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
        super().__init__('Exp')
        super().__init__(False, treecanvas, level, parent, left, right, 'Exp')


    def propagate(self,input):
        children = [] 
        if input == '(' or  Rule.check_identifier(input) or Rule.check_int(input) :
            children = [ Term ,ExpDash ]
            super().add_children(children)
            children = super().get_children()
        else:
            self.raise_exception()


        return children

class ExpDash(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__( 'Exp\'')
        super().__init__(False, treecanvas, level, parent, left, right, 'Exp\'')


    def propagate(self,input):
        children = []
        if input == '+':
            children = [Addop,Term]   
        elif input=='-':
            children = [Addop,Term]
        elif input ==')'or input =='$' :
            children = [EpsilonTerminal]
        else:
            self.raise_exception()

        if children:
            super().add_children(children)
            children = super().get_children()


        return children

class Addop(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__( 'Addop')
        super().__init__(False, treecanvas, level, parent, left, right, 'Addop')

    def propagate(self,input):
        children = []
        if input == '+':
            children = [plusTerminal]
        elif input=='-':
            children = [minusTerminal]
        else:
            self.raise_exception()

        if children:
            super().add_children(children)
            children = super().get_children()

        return children

class Mullop(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__( 'Mullop')
        super().__init__(False, treecanvas, level, parent, left, right, 'Mullop')

    def propagate(self,input):
        children = []
        if input == '*':
            children = [multiplyTerminal]
        elif input=='/':
            children = [divisionTerminal]
        else:
            self.raise_exception()

        if children:
            super().add_children(children)
            children = super().get_children()


        return children

class Factor(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__( 'Factor')
        super().__init__(False, treecanvas, level, parent, left, right, 'Factor')

    def propagate(self,input):
        children = []
        reset_label = False
        if input == Rule.check_identifier(input):
            children = [IDTerminal]
            reset_label = True
        elif input==Rule.check_int(input):
            children = [NumTerminal]
            reset_label = True
        elif input=='(':
            children = [leftBracketTerminal,Exp,rightBracketTerminal]
        else:
            self.raise_exception()

        if children:
            super().add_children(children)
            children = super().get_children()
            if reset_label:
                children[0].set_label(input)


        return children

class Term(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__( 'Term')
        super().__init__(False, treecanvas, level, parent, left, right, 'Term')

    def propagate(self,input):
        children = []
        if input =='(' or input == Rule.check_identifier(input) or Rule.check_int(input) :
            children = [Factor,TermDash]
        else:
            self.raise_exception()

        if children:
            super().add_children(children)
            children = super().get_children()


        return children
        

class TermDash(TreeNodeDrawing,Rule):

    def __init__(self, treecanvas, level, parent, left, right,):
        super().__init__( 'Term\'')
        super().__init__(False, treecanvas, level, parent, left, right, 'Term\'')

    def propagate(self,input):
        children = []
        if input =='*' or input == '/':
            children = [Mullop,Factor]
        elif input =='+' or input =='-' or input ==')' or input=='$':
            children = [EpsilonTerminal]
        else:
            self.raise_exception()

        if children:
            super().add_children(children)
            children = super().get_children()
        
        return children


    