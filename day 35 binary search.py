a = [102,93,39,29,49,17,48,27,48,18,440]
num = int(input("Enter the Number to be Searched : "))

beg = 0
end = len(a) - 1
while beg <= end:
    mid = (beg+end) // 2
    if a[mid] == num:
        print("\nFound at Position : ", mid + 1)
        break
    elif num > a[mid]:
        beg = mid + 1
    elif num < a[mid]:
        end = mid - 1
else:
    print("\nNot Found")
