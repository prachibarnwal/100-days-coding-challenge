# Code to make a login screen using **tkinter** (GUI INTERFACE) :))
from tkinter import *

def greet1():
    n = nam.get()
    lres.configure(text="Welcome " + n)

def greet2():
    n = nam.get()
    lres.configure(text="Bye " + n)

parent = Tk() #parent is a variable name to create an object of Tk
parent.geometry("400x250")
parent.title("JAI HIND") #this will show the title

l1 = Label(parent,text = "NAME : ")
l1.place(x=10, y=50)
nam = Entry(parent)
nam.place(x=90,y=50)

lres = Label(parent,text="MESSAGE ")
lres.place(x = 90, y = 190)
tfv = Label(parent,text = "Thanks For Visiting")
tfv.place(x = 150, y = 230)

b1 = Button(parent,text="Login ",command = greet1)
b1.place(x = 30, y = 140)
b2 = Button(parent,text="Logout ",command = greet2)
b2.place(x = 100, y = 140)

parent.mainloop()  #line to stop a code 
