'''
sum of series like
        x + x^2 + x^3 + ..... + x^n
'''
x = int(input("Enter Value of x : "))
n = int(input("Enter Value of n : "))
s = 0
for a in range(1, n + 1):
    if a < n:
        print(str(x) + "^" + str(a), end = ' + ')
    else:
        print(str(x) + "^" + str(a))
    s += x ** a
print("Sum of Series is : ",s)
