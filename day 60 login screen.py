for k in range(3):
    userid = input("Enter the User Id : ")
    pwd = input("Enter the Password : ")
    if userid.lower() == 'prachi' and pwd.lower() == 'anjali':
        print("Password Matched !!!")
        print("Access Granted")
        break
    else:
        print("INVALID USER ID/ PASSWORD")
else:
    print("Access Denied")
