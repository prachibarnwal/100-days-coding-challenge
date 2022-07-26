num = int(input("Enter a number : "))
p = 1
for i in range(num,0,-1):
    p *= i
print("Factorial of ", num, " is ", p)
