def factorial(num):
    if num == 1:
        return 1
    res = num * factorial(num-1)
    return res
n = int(input("Enter a  Number : "))
r = factorial(n)
print("FACTORIAL  OF  ",n,"  IS  ",r)
