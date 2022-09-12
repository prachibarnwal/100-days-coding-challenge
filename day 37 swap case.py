a = list(eval(input("Enter the list of Values : ")))
print("List Before Swapping : ",a)
for i in range(0,len(a),2):
    if i+1 < len(a):
        a[i],a[i+1] = a[i+1],a[i]
print("List After Swap is : ",a)
