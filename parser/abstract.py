from parser.terminals import *

class AbstractSyntaxAnalyzer:

    def __init__(self,terminals,treecanvas,width):

        self.__terminals = terminals
        self.__tree_canvas = treecanvas
        self.__width =  max(width,self.__tree_canvas.winfo_width()) 
        self.__filter()
        self.__generate_tree()

    def __filter(self):
        
        list = []
        for terminal in self.__terminals:
            if isinstance(terminal,(IDTerminal,NumTerminal,plusTerminal,minusTerminal,multiplyTerminal,divisionTerminal)):
                list.append(terminal)
        self.__terminals = list

    def __generate_tree(self):
        
        i = 1
        parent = self.__terminals[i].__class__(self.__tree_canvas,0,None,0,self.__width)
        parent.draw()
        while i < len(self.__terminals):
            if i+2 >= len(self.__terminals):
                parent.add_children([self.__terminals[i-1].__class__,self.__terminals[i+1].__class__])
                children = parent.get_children()
                children[0].set_label(self.__terminals[i-1].__str__())
                children[1].set_label(self.__terminals[i+1].__str__())
            else:    
                parent.add_children([self.__terminals[i-1].__class__,self.__terminals[i+2].__class__])
                children = parent.get_children()
                children[0].set_label(self.__terminals[i-1].__str__())
                parent = children[1]
            i+=2