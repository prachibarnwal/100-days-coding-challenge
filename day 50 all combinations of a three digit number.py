a = [0,0,0]
a[0] = int(input("Enter First Digit : "))
a[1] = int(input("Enter Second Digit : "))
a[2] = int(input("Enter Third Digit : "))
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                print(a[i],a[j],a[k])
