from tkinter import *
import tkinter as tk
import os
import sqlite3

import GUI_functions
import GUI121_main

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(700,300)
        self.master.maxsize(700,300)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
  












            




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
