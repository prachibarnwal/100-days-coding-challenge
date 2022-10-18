def isValidName(name):
    for ch in name:
        if not (ch.isalpha() or ch == " "):
            return False
    else:
        return True
txt = input("Enter Name to Validate : ")
if isValidName(txt):
    print(txt,"is a Valid Name.")
else:
    print(txt,'is not a Valid Name')
