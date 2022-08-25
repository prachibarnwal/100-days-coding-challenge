n = int(input("Enter the number of Rows : "))
for i in range(n, 0, -1):
    for a in range(1, i + 1):
        print(chr(64+a), end = " ")
    print()
