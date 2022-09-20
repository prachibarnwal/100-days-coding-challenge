a = list(eval(input("Enter a List of Numbers : ")))
print("List Before Sorting : ",a)

n = len(a)
for i in range(n - 1):
    for j in range(0,n - 1 - i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("List After Sorting : ",a)
