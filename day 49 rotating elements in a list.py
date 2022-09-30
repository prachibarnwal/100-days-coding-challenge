a = list(eval(input("Enter a List of Numbers : ")))
n = int(input("Enter the Number of Elements to be Shifted : " ))
print(a)
for i in range(n):
    temp = a[0]
    for j in range(len(a) - 1):
        a[j] = a[j+1]
    a[-1] = temp
print(a)


'''
OR
a = list(eval(input("Enter a List of Numbers : ")))
n = int(input("Enter the Number of Elements to be Shifted : " ))
print(a)
a = a[n:] + a[:n]
print(a)

OR

a = list(eval(input("Enter a List of Numbers : ")))
n = int(input("Enter the Number of Elements to be Shifted : " ))
print(a)
for i in range(n):
    temp = a.pop(0)
    a.append(temp)
print(a)
'''
