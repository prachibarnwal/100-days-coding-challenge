import pickle
import os
def addContact():
    name = input("Enter Name : ")
    phone = input("Enter Phone Number : ")
    data = [name,phone]
    f = open("contacts.dat","ab")
    pickle.dump(data,f)
    f.close()
    print("SUCCESSFULLY ADDED")
def display():
    f = open("contacts.dat","rb")
    print("-"*40)
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            print(data[0]+"\t\t"+data[1])
    except:
        f.close()
def search():
    name = input("Enter Name to be Searched : ")
    f = open("contacts.dat","rb")
    print("-"*40)
    n = 0
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print(data[0]+"\t\t"+data[1])
                n += 1
    except:
        if n == 0:
            print("No Such Contact Found")
        f.close()
def update():
    name = input("Enter Name to be Updated : ")
    f = open("contacts.dat","rb")
    g = open("temp.dat","wb")
    print("-"*40)
    n = 0
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print(data[0]+"\t\t"+data[1])
                phone = input("Enter the Modified Phone Number : ")
                data[1] = phone
                n += 1
            pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No Such Contact Found")
        else:
            os.remove("contacts.dat")
            os.rename("temp.dat","contacts.dat")
        
    
def delete():
    name = input("Enter Name to be Deleted : ")
    f = open("contacts.dat","rb")
    g = open("temp.dat","wb")
    print("-"*40)
    n = 0
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print("DELETED RECORD : "+data[0]+"\t\t"+data[1])
                n += 1
            else:
                pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No Such Contact Found")
        else:
            os.remove("contacts.dat")
            os.rename("temp.dat","contacts.dat")
        f.close()

while True:
    print("-"*40)
    print("Press 1 - Add a New Contact")
    print("Press 2 - Display All Contacts")
    print("Press 3 - Search a Contact")
    print("Press 4 - Delete a Contact")
    print("Press 5 - Update a Contact")
    print("Press 6 - to Exit")
    print("-"*40)
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        addContact()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        delete()
    elif ch == 5:
        update()
    else:
        break
    
