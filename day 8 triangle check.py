while True:
    print("Press 1 - to check a triangle")
    print("Press 2 - to exit")
    ch = int(input("Enter your Choice : "))
    if ch == 1:
        a = int(input("Enter First Side : "))
        b = int(input("Enter Second Side : "))
        c = int(input("Enter Third Side : "))
        if a == b and b == c:
            print("Triangle is EQUILATERAL")
        elif a == b or b == c or c == a:
            print("Triangle is ISOSCELES")
        else:
            print("Triangle is Scalene")
    elif ch == 2:
        print("Thanks For Visiting")
        break
    else:
        print("2 hi choices di gyi thi aapko.....teesra to koi option hi nhi tha >_<")
