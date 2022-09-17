a = list(eval(input("Enter a List of Numbers : ")))
m = 0
for num in a:
    if num > m:
        m = num
res = 0
for num in a:
    if num != m and num > res:
        res = num
print("Second highest is : ", res)
