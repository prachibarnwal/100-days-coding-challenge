pwd = input("Enter the Required Password : ")
n = len(pwd)
if n >= 8 and n <= 16:
    c = 0
    s = 0
    d = 0
    b = 0
    a = 0
    for ch in pwd:
        if ch.isupper():
            c += 1
        elif ch.islower():
            s += 1
        elif ch.isdigit():
            d += 1
        elif ch in "~!@#$%^*^()_-{[}];:'<>.,/?":
            b += 1
        else:
            a += 1
            break
    if a != 0:
        print("INVALID PASSWORD")
    else:
        if c > 0 and s > 0 and d > 0 and b > 0:
            print("PASSWORD STRENGTH IS STRONG")
        else:
            print("WEAK PASSWORD")
else:
    print("PASSWORD MUST HAVE MINIMUM OF 8 CHARACTERS AND MAXIMUM OF 16")
