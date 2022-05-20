import tkinter as tk, tkinter.ttk as ttk
from typing import Iterable

from tkinter import *
   
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
        self.title('Table Window')
        self.__rows = rows
        
        self.scrollframe = ScrollFrame(self, 10, 2, 0, cspan=3).colcfg(range(3), weight=1).frame
        
        self.fillScrollRegion()
                

    def fillScrollRegion(self):
        for row in range(len(self.__rows)):
            for j in range(len(self.__rows[0])):
                e = tk.Entry(self.scrollframe, width=30,
                            font=('Arial',16,'bold'))      
                e.grid(row=row, column=j,sticky=(N,W,E,S))
                e.insert(tk.END, str(self.__rows[row][j]))
                e.config(state=tk.DISABLED,disabledbackground="white",disabledforeground='black')
