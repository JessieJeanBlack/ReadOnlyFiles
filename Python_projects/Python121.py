from tkinter import *
import tkinter as tk
import os
import sqlite3

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(700,300)
        self.master.maxsize(700,300)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
        
    def load_gui(self): 
        self.btn_browse1 = tk.Button(self.master,width=12,height=2,text='Browse')
        self.btn_browse1.grid(row=3,column=0,padx=(2,210),pady=(20,100),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Browse')
        self.btn_browse1.grid(row=4,column=0,padx=(2,210),pady=(40,80),sticky=W)












            




if __name__ = "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
