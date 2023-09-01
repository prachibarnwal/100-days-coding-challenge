from tkinter import *
def check():
    un  = nametxt.get()
    pwd = pwdtxt.get()
    print("Username Entered : ",un)
    print("Password Entered : ",pwd)

#window
win = Tk()
win.geometry("500x250")
win.title("Login Form")

#username
name = Label(win, text = "User Name : ")
name.grid(row=0,column = 0)
nametxt = Entry(win)
nametxt.grid(row = 0, column = 1)

#password
pwd = Label(win,text = "Password")
pwd.grid(row= 1, column = 0)
pwdtxt = Entry(win, show = "*")
pwdtxt.grid(row = 1,column =1 )

#login button
btnl = Button(win,text="Login",command = check)
btnl.grid(row = 3,column = 0)

win.mainloop()
