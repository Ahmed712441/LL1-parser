import tkinter as tk, tkinter.ttk as ttk
from typing import Iterable
from parsers.terminals import *
from parsers.grammar import *
from parsers.parser import Parser
from tkinter import *

TERMINALS = [plusTerminal,minusTerminal,leftBracketTerminal,rightBracketTerminal,multiplyTerminal,divisionTerminal,
                        dollarTerminal,IDTerminal,NumTerminal]

RULES = [Exp,ExpDash,Addop,Mullop,Factor,Term,TermDash]


class ScrollFrame(tk.Frame):
    def __init__(self, master, scrollspeed=5, r=0, c=0, rspan=1, cspan=1, grid={}, **kwargs):
        tk.Frame.__init__(self, master, **{'width':400, 'height':300, **kwargs})
        
        #__GRID
        self.grid(**{'row':r, 'column':c, 'rowspan':rspan, 'columnspan':cspan, 'sticky':'nswe', **grid})
        
        #allow user to set width and/or height
        if {'width', 'height'} & {*kwargs}:
            self.grid_propagate(0)
            
        #give this widget weight on the master grid
        self.master.grid_rowconfigure(r, weight=1)
        self.master.grid_columnconfigure(c, weight=1)
        
        #give self.frame weight on this grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #_WIDGETS
        self.canvas = tk.Canvas(self, bd=0, bg=self['bg'], highlightthickness=0, yscrollincrement=scrollspeed)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        
        self.frame    = tk.Frame(self.canvas, **kwargs)
        self.frame_id = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        
        vsb = tk.Scrollbar(self, orient="vertical")
        vsb.grid(row=0, column=1, sticky='ns')
        vsb.configure(command=self.canvas.yview)
        
        #attach scrollbar to canvas
        self.canvas.configure(yscrollcommand=vsb.set)

        #_BINDS
        #canvas resize
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        #frame resize
        self.frame.bind("<Configure>", self.on_frame_configure)
        #scroll wheel       
        self.canvas.bind_all('<MouseWheel>', self.on_mousewheel)
        
    #makes frame width match canvas width
    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.frame_id, width=event.width)
        
    #when frame dimensions change pass the area to the canvas scroll region
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    #add scrollwheel feature
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-event.delta / abs(event.delta)), 'units')

    #configure self.frame row(s)
    def rowcfg(self, index, **options):
        index = index if isinstance(index, Iterable) else [index]
        for i in index:
            self.frame.grid_rowconfigure(i, **options)
        #so this can be used inline
        return self
        
    #configure self.frame column(s)
    def colcfg(self, index, **options):
        index = index if isinstance(index, Iterable) else [index]
        for i in index:
            self.frame.grid_columnconfigure(i, **options)
        #so this can be used inline
        return self

class TableWindow(tk.Toplevel):
    
    def __init__(self, master,rows, **kwargs):
        tk.Toplevel.__init__(self, master, **kwargs)
        self.geometry('700x500+600+200')
        self.attributes('-topmost', True)
        self.title('Action Table Window')
        self.__rows = rows
        
        self.scrollframe = ScrollFrame(self, 10, 0, 0, cspan=3).colcfg(range(3), weight=1).frame
        
        self.fillScrollRegion()
                

    def fillScrollRegion(self):
        for row in range(len(self.__rows)):
            for j in range(len(self.__rows[0])):
                e = tk.Entry(self.scrollframe, width=30,
                            font=('Arial',16,'bold'))      
                e.grid(row=row, column=j,sticky=(N,W,E,S))
                e.insert(tk.END, str(self.__rows[row][j]))
                e.config(state=tk.DISABLED,disabledbackground="white",disabledforeground='black')




class ParseTableWindow(tk.Toplevel):
    
    def __init__(self, master, **kwargs):
        tk.Toplevel.__init__(self, master, **kwargs)
        w = master.winfo_screenwidth()
        self.geometry(f'{w}x500+0+0')
        self.attributes('-topmost', True)
        self.title('Parse Table Window')
        
        self.scrollframe = ScrollFrame(self, 10, 2, 0, cspan=len(TERMINALS)+1).colcfg(range(len(TERMINALS)+1), weight=1).frame
        self.fill_first_row()
        self.fill_first_column()
        self.fillScrollRegion()

    def fill_first_row(self):
        for column in range(len(TERMINALS)):
            obj = TERMINALS[column](None, 0, None, 0, 0)
            e = tk.Entry(self.scrollframe, width=20,
                            font=('Arial',12,'bold'))      
            e.grid(row=0, column=column+1,sticky=(N,W,E,S))
            e.insert(tk.END, obj.__str__())
            e.config(state=tk.DISABLED,disabledbackground="white",disabledforeground='black')

    def fill_first_column(self):
        for row in range(len(RULES)):
            obj = RULES[row](None, 0, None, 0, 0)
            e = tk.Entry(self.scrollframe, width=30,
                            font=('Arial',12,'bold'))      
            e.grid(row=row+1, column=0,sticky=(N,W,E,S))
            e.insert(tk.END, obj.__str__())
            e.config(state=tk.DISABLED,disabledbackground="white",disabledforeground='black')

    @staticmethod
    def join(list):
        str = ''
        for i in range(len(list)):
            obj = list[i](None, 0, None, 0, 0)
            str += obj.__str__()
        return str

    def fillScrollRegion(self):

        for row in range(len(RULES)):
            obj = RULES[row](None, 0, None, 0, 0)
            for column in range(len(TERMINALS)):
                ter = TERMINALS[column](None, 0, None, 0, 0)
                try:
                    children = obj.rule_dict[ter.__str__()]
                    str = ParseTableWindow.join(children)
                    e = tk.Entry(self.scrollframe, width=40,
                            font=('Arial',12,'bold'))      
                    e.grid(row=row+1, column=column+1,sticky=(N,W,E,S))
                    e.insert(tk.END, str)
                    e.config(state=tk.DISABLED,disabledbackground="white",disabledforeground='black')
                except :
                    e = tk.Entry(self.scrollframe, width=30,
                            font=('Arial',12,'bold'))      
                    e.grid(row=row+1, column=column+1,sticky=(N,W,E,S))
                    e.config(state=tk.DISABLED,disabledbackground="white",disabledforeground='black')

                     