from tkinter import filedialog
from tkinter import *
import os
import sqlite3
root = Tk()

        
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(450,200)
        self.master.maxsize(450,200)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")

        def center_window(self, w, h):
            screen_width = self.master.winfo_screen

if __name__ == "__main__":
    root.mainloop()
    print(folder_path)


