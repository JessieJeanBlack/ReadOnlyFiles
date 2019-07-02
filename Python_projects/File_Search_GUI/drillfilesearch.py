import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3


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


        self.varB1 = StringVar()
        self.varB2 = StringVar()

        self.txtB1 = Entry(self.master,text=self.varB1, font=('Helvetica', 12), fg='black', bg='white')
        self.txtB1.grid(row=3, column = 2, padx=(10,20), pady=(30,10))

        self.txtB2 = Entry(self.master, text=self.varB2, font=('Helvetica', 12), fg='black', bg='white')
        self.txtB2.grid(row=5, column = 2, padx=(10,20), pady=(10,20))

        self.btnSearch1 = Button(self.master, text='Browse', font=('Helvetica', 12), fg='black', bg='white')
        self.btnSearch1.grid(row=3, column=1, padx=(10,20), pady=(30,10), sticky=NE, command=browse_button)

        self.btnSearch2 = Button(self.master, text='Browse', font=('Helvetica, 12'), fg='black', bg='white')
        self.btnSearch2.grid(row=5, column=1, padx=(10,20), pady=(10,20), sticky=NE, command=browse_button)
        
    def source(self):
        sourceFilePath = filedialog.askdirectory(initialdir="/", title='Select Source')
        
    def destination(self):
        destinationFilePath = filedialog.askdirectory(initialdir="/", title='Select Destination')


    def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    return filename

    def source:
        sourcepath = tk.filedialog.askdirectory()
        self.txtB1.update()
        self.txtB1.config(state="normal")
        self.txtB1.delete(0, END)
        self.txtB1.insert(INSERT, sourcepath)
        self.txtB1.config(state="disabled")


    def moveFiles(self):
        print("Move")
        sourceDir = self.txtB1.get()
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
                sourceFile = os.path.join(sourceDir, file)
                destFile = os.path.join(destDir, file)
                shutil.move(sourceFile, destDir)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(destFile))
                fmd.logMove(batch, destFile, mtime)
        fmd.printLogs(batch)

    def closeProgram(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
