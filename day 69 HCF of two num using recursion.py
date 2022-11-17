def HCF(n1,n2):
    if n1 % n2 == 0:
        return n2
    res = HCF(n2, n1 % n2)
    return res
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
res = HCF(a,b)
print("HCF OF ",a," AND ",b," IS ",res)
