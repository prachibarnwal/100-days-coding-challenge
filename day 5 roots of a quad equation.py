a = float(input("Enter Coefficient of A : "))
b = float(input("Enter Coefficient of B : "))
c = float(input("Enter Coefficient of C : "))
d = b ** 2  -  4 * a * c

if d < 0:
    print("NO REAL ROOTS ARE THERE...!")
elif d == 0:
    r1 = r2 = -b / (2 * a)
    print("Real and Equal Roots are : ", r1, r2)
else:
    r1 = (-b + d ** 0.5) / (2 * a)
    r2 = (-b - d ** 0.5) / (2 * a)
    print("Real and Unequal Roots are : ",round(r1,2), " and ", round(r2,2))


    
