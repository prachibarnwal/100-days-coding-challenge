import math
num = int(input("Enter  a Number : "))
s = 0
a = num
while num > 0:
    d = num % 10
    s += math.factorial(d)
    num //= 10
if s == a:
    print("STRONG NUMBER")
else: print("NOT A STRONG NUMBER ")
