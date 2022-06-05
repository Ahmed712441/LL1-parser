import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.__str__()
sys.path.append(BASE_DIR)


from tkinter import *
from GUI.settings import *
from tkinter.ttk import *
from parsers.grammar import *
from parsers.parser import Parser
from tkinter import messagebox
from GUI.tree import TreeCanvas
from GUI.table import TableWindow,ParseTableWindow
from parsers.abstract import AbstractSyntaxAnalyzer




class Main(Frame):

    def __init__(self,root):
        Frame.__init__(self, root)
        self.__str_label =  Label(self,text = "Enter your String :")
        self.__str_entry = Entry(self)
        self.__submit_string = Button(self ,text="Submit String" , command=self.__submit)
        self.canvas = TreeCanvas(self)
        self.abstractcanvas = TreeCanvas(self)
        self.__actions = None
        self.__parser =  Parser(self.canvas.canvas,Exp)
        self.__show_button = Button(self ,text="Show Action Table" , command=self.__show_table)
        self.__show_abstract = Button(self ,text="Show Abstract Tree" , command=self.__show_abstract_tree)
        self.__show_parse = Button(self ,text="Show parse Tree" , command=self.__show_parse_tree)
        self.__show_parse_button = Button(self ,text="Show parse Table" , command=self.__show_parse_table)
        self.__pack_on_screen()
    
    def __show_parse_table(self):
        ParseTableWindow(self)

    def __show_table(self):
        if self.__actions:
            TableWindow(self,rows=self.__actions)
    
    def __show_abstract_tree(self):
        self.canvas.grid_forget()
        self.abstractcanvas.grid(row=1,column=0,columnspan=6,sticky=(N,W,E,S))
        self.__show_abstract.grid_forget()
        self.__show_parse.grid(row=0,column=4,sticky=(N,W,E,S))

    def __show_parse_tree(self):
        self.abstractcanvas.grid_forget()
        self.canvas.grid(row=1,column=0,columnspan=6,sticky=(N,W,E,S))
        self.__show_parse.grid_forget()
        self.__show_abstract.grid(row=0,column=4,sticky=(N,W,E,S))

    def __pack_on_screen(self):
        self.__str_label.grid(column=0,row=0,sticky=(N,W,E,S))
        self.__str_entry.grid(row=0,column=1,sticky=(N,W,E,S))
        
        self.__submit_string.grid(row=0,column=2,sticky=(N,W,E,S))
        self.__show_button.grid(row=0,column=3,sticky=(N,W,E,S))
        self.__show_abstract.grid(row=0,column=4,sticky=(N,W,E,S))
        self.__show_parse_button.grid(row=0,column=5,sticky=(N,W,E,S))
        self.canvas.grid(row=1,column=0,columnspan=6,sticky=(N,W,E,S))
        
        
        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=4)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)
        self.columnconfigure(5,weight=1)
        self.rowconfigure(1,weight=1)

    def __submit(self):
        
        try:
            self.canvas.canvas.delete("all") 
            self.abstractcanvas.canvas.delete("all")
            self.__actions = []
            self.__actions.append(['Stack','Input','Action'])
            terminals = self.__parser.parse(self.__str_entry.get(),self.__actions)
            AbstractSyntaxAnalyzer(terminals,self.abstractcanvas.canvas,self.canvas.canvas.winfo_width())
        except Exception as e:
            print(e)
            self.canvas.canvas.delete("all")
            messagebox.showerror(title="Parse Error",message="Your string can\'t be parsed check action table for details")   

if __name__ == "__main__":
    
    root =  Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 1200 if w > 1200 else w
    h = 720 if h > 720 else h
    root.geometry("%dx%d+0+0" % (w, h))

    root.title('LL(1) Parser')

    can = Main(root)
    
    can.grid(row=0,column=0,sticky = "NSEW")
    
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    root.mainloop()