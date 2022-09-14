a = list(eval(input("Enter a List of Numbers : ")))
i = 0
print("List before removing : ",a)

while i < len(a):
    if a.count(a[i]) > 1:
        a.remove(a[i])
    else:
        i += 1
        

print("List after removing : ",a)
