import os

#Python:    3.7.3
#
#Author:    Jessie J. Black
#
#Purpse:    Create a directiory with 10 different files of varying types, including at least two .txt text documents.
#
#           Create a script using Python and the OS module using the listdir() method to iterate through
#           all of the files in specified directory. Use path.join() method to concatenate the file name
#           to it's file path, forming an absolute path. Use the getmtime() method to find the latest date 
#           that each text document has been created or modified. Print each file ending with .txt file
#           extension and its corresponding mtime to the console.

fName = 'godCalledInSick.txt'

f1Name = 'Unintended.txt'

f2Name = 'darkEnergy.html'

f3Name = 'Multiverse.html'

f4Name = 'aimlessEvolution.jpg'

f5Name = 'Probial.jpg'

f6Name = 'Luca.html'

f7Name = 'vanillasky.pdf'

f8Name = 'AmericanPsycho.html'

f10Name = 'HollywoodTeaser.html'

fPath = 'C:\\montPython\\'
        

abPath = os.path.join(fPath, fName)
print(abPath)

f1 = open('godCalledInSick.txt', 'r')
file_content = f1.read()
print(file_content)

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("godCalledInSick.txt")))
print("Created: %s" % time.ctime(os.path.getctime("godCalledInSick.txt")))

acPath = os.path.join(fPath, f1Name)
print(acPath)

f = open('Unintended.txt', 'r')
file_contents = f.read()
print(file_contents)

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("Unintended.txt")))
print("Created: %s" % time.ctime(os.path.getctime("Unintended.txt")))


adPath = os.path.join(fPath, f2Name)
print(adPath)

aePath = os.path.join(fPath, f3Name)
print(aePath)

afPath = os.path.join(fPath, f4Name)
print(afPath)

agPath = os.path.join(fPath, f5Name)
print(agPath)

ahPath = os.path.join(fPath, f5Name)
print(ahPath)

aiPath = os.path.join(fPath, f6Name)
print(aiPath)

ajPath = os.path.join(fPath, f7Name)
print(ajPath)

akPath = os.path.join(fPath, f8Name)
print(akPath)

amPath = os.path.join(fPath, f10Name)
print(amPath)


