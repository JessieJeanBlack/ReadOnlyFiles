from tkinter import *
import tkinter as tk
import os
import urllib.request
import sqlite3



    
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(700,400)
        self.master.maxsize(700,400)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
        
        def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
        # get user's screen width and height
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
        # calculate x and y coordinates to paint the app centered on the user's screen
            x = int((screen_width/2) - (w/2))
            y = int((screen_height/2) - (h/2))
            centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
