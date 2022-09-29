a = list(eval(input("Enter a List of  Numbers : ")))
b = list(eval(input("Enter a List of  Numbers : ")))
r = []
for ch in a:
    for ch2 in b:
        r.append((ch,ch2))
print(a)
print(b)
print(r)
