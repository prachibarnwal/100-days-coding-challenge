a  = list(eval(input("Enter a list of Numbers : ")))

n = len(a)
for i in range(n // 2):
    a[i], a[n-i-1] = a[n-i-1],a[i]
print(a)
