n = int(input("Enter the Number of Rows : "))
for a in range(1, n+1):
    for s in range(n - a):
        print(" ", end = " ")
    for t in range(2 * a - 1):
        print("*", end = " ")
    print()
