t = input("Enter a String : ")
res = ""
for ch in t:
    if ch.islower():
        res += ch.upper()
    elif ch.isupper():
        res += ch.lower()
    else:
        res += ch



print("Original String is : ",t)
print("Resultant String is : ",res)
