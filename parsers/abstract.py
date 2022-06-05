from tkinter import SEPARATOR
from parsers.terminals import *

class TempNode:

    def __init__(self,left,right,terminal) -> None:
        self.__left = left
        self.__right = right
        self.terminal = terminal


    def drawnode(self,canvas=None,level=0,parent=None,left=0,right=0,curr=None):
        if not curr:
            curr = self.terminal.__class__(canvas,level,parent,left,right)
            curr.draw()

        if self.__left:
            curr.add_children([self.__left.terminal.__class__])
            children = curr.get_children()
            children[0].set_label(self.__left.terminal.__str__())
            self.__left.drawnode(curr=children[0])
        
        if self.__right:
            curr.add_children([self.__right.terminal.__class__])
            children = curr.get_children()
            children[-1].set_label(self.__right.terminal.__str__())
            self.__right.drawnode(curr=children[-1])


class AbstractSyntaxAnalyzer:

    TERMINALS = (IDTerminal,NumTerminal,plusTerminal,minusTerminal,multiplyTerminal,divisionTerminal) # Terminals which will participate in abstract tree
    SEPARATOR = (leftBracketTerminal) # Terminal in which when found start new list of tokens which is treated as single element in old token ex: 2*(3*3) this will make your list = [2,*,[3,*,3]] instead of list = [2,*,3,*,3]
    TERMINATOR = (rightBracketTerminal) # Terminal in which End the separtor created list right bracket in my case  

    def __init__(self,terminals,treecanvas,width):

        self.__terminals = terminals
        self.__tree_canvas = treecanvas
        self.__width =  max(width,self.__tree_canvas.winfo_width()) 
        self.__filter()
        self.__generate()

    def __filter(self):
        
        list = []
        i = 0
        while i < len(self.__terminals):
            if isinstance(self.__terminals[i],self.TERMINALS):
                list.append(self.__terminals[i])
            elif isinstance(self.__terminals[i],self.SEPARATOR):
                lst = []
                while i < len(self.__terminals):
                    i+=1
                    if isinstance(self.__terminals[i],self.TERMINALS):
                        lst.append(self.__terminals[i])
                    elif isinstance(self.__terminals[i],self.TERMINATOR):
                        list.append(lst)
                        break
            i+=1 
        self.__terminals = list

    @staticmethod
    def largest_pirority(list):

        max_priority = 0
        for i in range(1,len(list)):
            if isinstance(list[i],TreeNode):
                if list[i].pirority >= list[max_priority].pirority :
                    max_priority = i

        return max_priority
                

    @staticmethod
    def generate_tree(list):
        if len(list) == 0:
            return None
        if len(list) == 1:
            if isinstance(list[0],TreeNode):
                return TempNode(None,None,list[0])
            else:
                list = list[0]
        split_index = AbstractSyntaxAnalyzer.largest_pirority(list)
        return TempNode(AbstractSyntaxAnalyzer.generate_tree(list[:split_index]),AbstractSyntaxAnalyzer.generate_tree(list[split_index+1:]),list[split_index])

    def __generate(self):
        root = AbstractSyntaxAnalyzer.generate_tree(self.__terminals)
        root.drawnode(self.__tree_canvas,0,None,0,self.__width)
    