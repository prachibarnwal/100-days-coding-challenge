n = input("Enter a string : ")
d = {}
for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for ch in d:
    print(ch," OCCURS ",d[ch]," TIMES")
