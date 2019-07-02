from tkinter import *
import csv
import tkinter
from tkinter import filedialog
root = Tk()
file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
if file != None:
    data = file.read()
    file.close()
    print("I got %d bytes from this file." % len(data))

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.filename=""
        csvfile=Label(root, text="File").grid(row=1, column=0)
        self.bar=Entry(master).grid(row=1, column=1)
        self.bar2=Entry(master).grid(row=3, column=1)
        self.master = master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")

        #Buttons  
        y=7
        self.bbutton= Button(root, text="OK", command=self.process_csv)
        y+=1
        self.bbutton.grid(row=10, column=3, sticky = W + E)
        self.cbutton= Button(root, text="Browse", command=self.browsecsv)
        self.cbutton.grid(row=1, column=3)

    def browsecsv(self):
        from tkFileDialog import askopenfilename

        Tk().withdraw() 
        self.filename = askopenfilename()

    def process_csv(self):
        if self.filename:
            with open(self.filename, 'rb') as csvfile:
                logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                rownum=0

                for row in logreader:    
                    NumColumns = len(row)        
                    rownum += 1

                Matrix = [[0 for x in xrange(NumColumns)] for x in xrange(rownum)] 

root = Tk()
window=Window(root)
root.mainloop()  
