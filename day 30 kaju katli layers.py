n = int(input("Enter the number of rows : "))
for a in range(n, 0, -1):
    for b in range(a):
        print("*",end = " ")
    for c in range(2 * (n - a)):
        print(" ",end = " ")
    for b in range(a):
        print("*", end = " ")
    print()
for a in range(1, n + 1):
    for b in range(a):
        print("*",end = " ")
    for c in range(2 * (n - a)):
        print(" ",end = " ")
    for b in range(a):
        print("*", end = " ")
    print()
