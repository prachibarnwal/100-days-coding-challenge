a = eval(input("Enter a list of Numbers : "))
num = int(input("Enter the Number to be Searched : "))
for i in range(len(a)):
    if a[i] == num:
        print("Found at Position ", i+1)
        break
else:
    print("Number not Found")
