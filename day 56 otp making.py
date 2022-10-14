import random
def generateotp():
    otp = []
    i = 0
    while i < 4:
        d = random.randint(0,9)
        if d not in otp:
            otp.append(d)
            i += 1
    return otp


otp = generateotp()
print("YOUR OTP IS : " ,end = " ")
for i in otp:
    print(i,end  = " ")
