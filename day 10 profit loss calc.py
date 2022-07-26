cp = float(input("Enter the COST PRICE : "))
sp = float(input("Enter the SELLING PRICE : "))
if sp > cp:
    print("Profit is Rs. ",sp-cp)
elif cp > sp:
    print("Loss is Rs. ",cp-sp)
else:
    print("No Profit No Loss")
