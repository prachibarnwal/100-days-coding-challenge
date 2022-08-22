for num in range(100,1000):
    a = num
    s = 0
    while a > 0:
        d = a % 10
        s += d ** 3
        a //= 10
    if s == num:
        print(num, " is Armstrong Number")
