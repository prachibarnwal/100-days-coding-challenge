#USING FOR LOOP
n = int(input("How many elements of Fibonacci Series are to be Printed : "))
a = 0
b = 1
if n >= 2:
    print(a, b, end = ' ')
    for i in range(n - 2):
        c = a + b
        print(c, end = ' ')
        a = b
        b = c



print("\n")
#USING WHILE LOOP
n = int(input("Enter the Highest limit of the Fibonacci Series : "))
a = 0
b = 1
c = a + b
print(a, b, end = ' ')
while c <= n:
    a = b
    b = c
    c = a + b
    print(c, end = ' ')
