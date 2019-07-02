import os

def writeData():
    data = '\nHello, world!'
    with open('text.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('text.txt', 'r') as f: #opening file and saving as f
        data = f.read() #creating file and storing what we read above
        print(data)#printing data to string
        f.close()#closed program



if __name__ == "__main__":
    writeData()
    openFile()
    
