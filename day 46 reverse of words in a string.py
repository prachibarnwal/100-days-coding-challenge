n = input("Enter a String : ")

d = n.split()
d = d[::-1]
res = ""
for i in d:
    res += i + " "
print(res)

res = " ".join(d)
print(res)
