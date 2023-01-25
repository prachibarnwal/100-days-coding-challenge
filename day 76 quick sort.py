def partition(a,left, right):
    i = left - 1
    pivot = right
    for j in range(left,right):
        if a[j] < a[pivot]:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[pivot] = a[pivot],a[i+1]
    return i + 1

def QuickSort(a,left,right):
    if right - left > 1:
        p = partition(a,left,right)
        QuickSort(a,left,p-1)
        QuickSort(a,p+1,right)
    else:
        return
n = list(eval(input("Enter A List of Numbers :")))
print("BEFORE SORTING : ")
print(n)
QuickSort(n,0,len(n)-1)
print("AFTER SORTING")
print(n)
