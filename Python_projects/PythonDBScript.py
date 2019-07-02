import sqlite3

conn = sqlite3.connect('my_Python.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_PythonDocs( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_document TEXT \
        )")
    conn.commit()
conn.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for file in fileList:
    if file.endswith(".txt"):
        conn = sqlite3.connect('my_Python.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_PythonDocs(col_document) VALUES(?)", (file, ))
        conn.commit()
        conn.close()
        print(file)
    from tkinter import *
    root = Tk()

    def browsefunc():
        filename = filedialog.askopenfilename()
        pathlabel.config(text=filename)

     def browse_button(self):
        filename = filedialog.askdirectory()
        print(filename)
        return(filename)
    
    def source(self):
        sourceFilePath = filedialog.askdirectory(initialdir="/", title='Select Source')
        self.txtB1.update()
        self.txtB1.config(state='normal')
        self.txtB1.delete(0, END)
        self.txtB1.insert(INSERT, sourceFilePath)
        self.txt.config(state='disabled')
        
    def destination(self):
        destinationFilePath = filedialog.askdirectory(initialdir="/", title='Select Destination')

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


browse_button = Button(root, text="Browse", command=browsefunc)
browse_button.pack()

pathlabel = Label(root)
pathlabel.pack()

    

path = '.\Python_projects'



    
