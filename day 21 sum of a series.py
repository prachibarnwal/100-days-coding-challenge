'''
to print sum of a series like
        1 + 1/2 + 13 + .... + 1/n
'''
n = int(input("Enter a Number : "))
s = 0
for i in range(1,n + 1):
    if i < n:
        print("1 / " + str(i), end = " + ")
    else:
        print("1 / " + str(i))
    s += 1 / i
print("Sum of Series is : ", round(s, 2))
