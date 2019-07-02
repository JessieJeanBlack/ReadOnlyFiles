from tkinter import *
import tkinter as tk
import os
import sqlite3

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        master = self.master


        # changing the title of our master widget      
        self.master.title("Check files")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        self.quitButton = Button(self, text="Browse...")

        # placing the button on my window
        self.quitButton.place(x=2, y=3)

root = Tk()

#size of the window
root.geometry("700x300")

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
 
