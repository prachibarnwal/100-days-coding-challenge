a = list(eval(input("Enter a List of Numbers : ")))
b = list(eval(input("Enter a List of Numbers : ")))
u = a.copy()
I = []
for i in b:
    if i not in a:
        u.append(i)
    else:
        I.append(i)
print("First List : ",a)
print("Second List : ",b)
print("Union of Both the Lists is : ",u)
print("Intersection of Both the Lists is : ",I)
