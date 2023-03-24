def LShift(Arr,n):
    for i in range(n):
        val = Arr.pop(0) # removes the first element
        Arr.append(val)
    print(Arr)

A = [10,20,30,40,50,60]
LShift(A,4)
