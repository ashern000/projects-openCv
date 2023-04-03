import cv2
import numpy as np
from tkinter import *
import tkinter as tk

root = tk.Tk()
mystring = tk.StringVar(root)
root.title("Filename")

def getvalue():
    imagePath = mystring.get()
    return imagePath

e1 = Entry(root, textvariable=mystring, width=50, fg="blue",
           bd=3, selectbackground='violet').pack()

button1 = tk.Button(root,
                text='Submit',
                fg='White',
                bg='dark green', height=10, width=10, command=getvalue and root.destroy).pack()


root.mainloop()


image = cv2.imread(getvalue())

continueWhile = ""

while continueWhile == "" or continueWhile=="yes":
    
   def getContinue():
        continueWhile = mystring.get()
        return str(continueWhile)
    
   continueWhile = getContinue()
   
   root =tk.Tk()
   root.title("Continue")
   
   mystring =tk.StringVar(root)
   
   with open("./myrois.txt", "a+") as f:
        f.write(str(cv2.selectROI(image)))
        f.write(", ")
   
   e1 = Entry(root, textvariable = mystring,width=50,fg="blue",bd=3,selectbackground='violet').pack()
   button1 = tk.Button(root,
                    text='Submit',
                    fg='White',
                    bg= 'dark green', height = 10, width = 10,command=getContinue and root.destroy).pack()    
   root.mainloop()
