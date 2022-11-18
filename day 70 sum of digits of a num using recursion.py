def sumofnum(num):
    if num == 0:
        return 0
    d = num % 10
    num //= 10
    res = d + sumofnum(num)
    return res
n = int(input("Enter a Number : "))
r = sumofnum(n)
print("SUM OF DIGITS OF ",n," IS ",r)
