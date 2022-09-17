a = list(eval(input("Enter a List of Numbers : ")))
n = len(a)
print("Before Swap List : ",a)
for i in range(n - 1):
    for j in range(i + 1,n):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("AFter Swap List : ",a)
