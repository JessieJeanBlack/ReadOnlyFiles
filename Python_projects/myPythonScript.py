import sqlite3
import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import datetime
from os import path
import Search_Comp

sourcepath = ""

def create_connection(my_Python):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(my_Python)
        return conn
    except Error as e:
        print(e)
    
def source(self):
    sourceFilePath = filedialog.askdirectory(initialdir="/", title='Select Source')
    self.txtB1.update()
    self.txtB1.config(state='normal')
    self.txtB1.delete(0, END)
    self.txtB1.insert(INSERT, sourceFilePath)
    self.txt.config(state='disabled')
        
def destination(self):
    destinationFilePath = filedialog.askdirectory(initialdir="/", title='Select Destination')
    self.txtB2.update()
    self.txtB2.config(state='normal')
    self.txtB2.delete(0, END)
    self.txtB2.insert(INSERT, destinationFilePath)
    self.txt.config(state='disabled')

def browse_button1(self):
    filename = filedialog.askdirectory()
    self.txtB1.insert(0,filename)  # Insert the 'path'
    print(filename)

def browse_button2(self):
    filename2 = filedialog.askdirectory()
    self.txtB2.insert(0,filename2)
    print(filename2)
    return(filename2)
    print(destinationFilePath)

 
def moveFiles(self):
    sourceDir = self.txtB1.get()
    destDir = self.txtB2.get()
    print("Move")
    if sourceDir == '':
        tkMessageBox.showinfo("Problem", "Please select a source directory!")
    if destDir == '':
        tkMessageBox.showinfo("Problem", "Please select a destination directory!")
    files = os.listdir(sourceDir)
    for file in files:
        if '.txt' in file:
            sourceFile = os.path.join(sourceDir, file)
            ntime = datetime.datetime.fromtimestamp(os.path.getmtime(sourceFile))
            destFile = os.path.join(destDir, file)
            shutil.move(sourceFile, destDir)
            print(ntime, file)
            conn = sqlite3.connect('my_Python.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_PythonDocs(col_document) VALUES(?)", (file, ))
            conn.commit()
            conn.close()
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #allows script to stay open until we close and kill window.





 
