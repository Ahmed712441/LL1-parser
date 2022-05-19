from sre_parse import State
import tkinter as tk
from tkinter import * 
from settings import *
import sys
from tkinter.ttk import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.__str__()
sys.path.append(BASE_DIR)


class TreeCanvas(Frame):

    def __init__(self,root,canvas_width=1000,canvas_height=10000):
        
        Frame.__init__(self, root) 
        self.count_nodes = 0 # this variable used to count nodes helpful in labeling nodes
        self.hor_scrollbar = Scrollbar(self, orient=HORIZONTAL)
        self.ver_scrollbar = Scrollbar(self, orient=VERTICAL) # height=height-20,width=width-20
        self.canvas = Canvas(self,background=CANVAS_BACKGROUND_COLOR,scrollregion=(0, 0, canvas_width, canvas_height),yscrollcommand=self.ver_scrollbar.set,xscrollcommand=self.hor_scrollbar.set) # canvas object
        self.hor_scrollbar['command'] = self.canvas.xview
        self.ver_scrollbar['command'] = self.canvas.yview
        self.pack_on_screen()
    
    def pack_on_screen(self):
        self.canvas.grid(row=0,column=0,sticky=(N,W,E,S))  # places the canvas in row : 0 , column :0 in the frame
        self.hor_scrollbar.grid(column=0, row=1, sticky=(W,E))
        self.ver_scrollbar.grid(column=1, row=0, sticky=(N,S))
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

class Table(Frame):
     
    def __init__(self,root):
        Frame.__init__(self, root)
        self.__row = 0
        self.insert_row(['Stack','Input','Action'])
    
    def insert_row(self,row):
        # 
        for i in range(len(row)):
            e = tk.Entry(self, width=20,
                        font=('Arial',16,'bold'))      
            e.grid(row=self.__row, column=i)
            e.insert(END, row[i])
            e.config(state=DISABLED,disabledbackground="white",disabledforeground='black')
            # e.config(background="white")
        
        self.__row +=1

        

class Main(Frame):

    def __init__(self,root):
        Frame.__init__(self, root)
        self.__str_label =  Label(self,text = "Enter your String :")
        self.__str_entry = Entry(self)
        self.__submit_string = Button(self ,text="Submit String" , command=self.__submit)
        self.canvas = TreeCanvas(self)
        self.table = Table(self)
        self.__pack_on_screen()

    def __pack_on_screen(self):
        self.__str_label.grid(column=0,row=0)
        self.__str_entry.grid(row=0,column=1)
        self.__submit_string.grid(row=0,column=2)
        self.canvas.grid(row=1,column=0)
        self.table.grid(row=1,column=1)

    def __submit(self):
        pass

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