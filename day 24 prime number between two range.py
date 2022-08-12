#start = int(input("Enter the Starting Number : "))
#end = int(input("Enter the Ending Number : "))
for num in range(100,1000):
    for a in range(2, num):
        if num % a == 0:
            break
    else:
        print(num, " is Prime ")
