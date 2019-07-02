import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3
import myPythonScript
import shutil





sourcepath = ""

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(350, 200))
        self.master.title('Search Files')
        self.master.config(bg='lightgray')


        entry1 = StringVar()
        entry2 = StringVar()

        self.txtB1 = Entry(self.master,textvariable=entry1, font=('Helvetica', 12), fg='black', bg='white')
        self.txtB1.grid(row=3, column = 2, padx=(10,20), pady=(30,10))

        self.txtB2 = Entry(self.master, textvariable=entry2, font=('Helvetica', 12), fg='black', bg='white')
        self.txtB2.grid(row=5, column = 2, padx=(10,20), pady=(30,20))

        self.btnSearch1 = Button(self.master, text='Browse', font=('Helvetica', 12), fg='black', bg='white', command=lambda:myPythonScript.browse_button1(self))
        self.btnSearch1.grid(row=3, column=1, padx=(10,20), pady=(30,10), sticky=NE)

        self.btnSearch2 = Button(self.master, text='Browse', font=('Helvetica', 12), fg='black', bg='white', command=lambda:myPythonScript.browse_button2(self))
        self.btnSearch2.grid(row=5, column=1, padx=(10,20), pady=(30,10), sticky=NE)

        self.move_files = Button(self.master, text='Move Files', font=('Helvetica, 12'), fg='black', bg='white', command=lambda:myPythonScript.moveFiles(self))
        self.move_files.grid(row=7, column=1, padx=(30,10), pady=(30,10), sticky=NE)


    
        
    
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #allows script to stay open until we close and kill window.
