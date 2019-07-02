import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3
import drillfilesearch.py


root = tk.Tk()
root.overrideredirect(1)
root.withdraw()

root =Tk()
sourcepath = ""

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(350, 160))
        self.master.title('Search Files')
        self.master.config(bg='lightgray')

    def folderSelector(txtB1):
        sourcepath = tk.filedialog.askdirectory()
        self.txtB1.update()
        self.txtB1.config(state="normal")
        self.txtB1.delete(0, END)
        self.txtB1.insert(INSERT, sourcepath)
        self.txtB1.config(state="disabled")

    def dirSelect1(txtB2):
        folderSelector(self.txt_B2)

    def moveFiles(self):
        print("Move")
        sourceDir = self.txtB2.get()
        destDir = self.txtB2.get()

        print(sourceDir)
        print(destDir)

        if sourceDir == '':
            tk.messagebox.showinfo("Problem", "Please select a source directory!")
            return
        if destDir == '':
            tk.messagebox.showinfo("Problem", "Please select a destination directory!")
            return
        batch = datetime.datetime.now()
        files = os.listdir(sourceDir)
        for file in files:
            if file.endswith(".txt"):
                sourceFile = os.path.join(sourceDir, file)
                destFile = os.path.join(destDir, file)
                shutil.move(sourceFile, destDir)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(destFile))
                fmd.logMove(batch, destFile, mtime)
        fmd.printLogs(batch)

    def closeProgram(self):
        root.destroy()
