a = int(input("Enter the Upper Limit : "))
for num in range(1,a + 1):
    sq = num ** 2
    n = len(str(num))
    end = sq % 10 ** n
    if end == num:
        print(num)
