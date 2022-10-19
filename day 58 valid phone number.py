def isPhoneValid(num):
    if len(num) != 10:
        return False
    elif not num.isdigit():
        return False
    elif num[0] not in ("6789"):
        return False
    else:
        return True
num = input("Enter Phone Number : ")
if isPhoneValid(num):
    print("VALID PHONE NUMBER")
else:
    print("INVALID PHONE NUMBER")
