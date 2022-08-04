a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
while a % b != 0:
    rem = a % b
    a = b
    b = rem

print("HCF is : ",b)
