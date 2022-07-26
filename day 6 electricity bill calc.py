import time
print("\tWelcome to the Bill Calculating Code..!")
print("\n","*"*40)
units = int(input("Enter the number of units consumed : "))
print("\n","*"*40)
print("Calculating the Bill...")
for i in range(5):
    time.sleep(1)
    print(".",end = " ")
if units < 200:
    bill = 4 * units
elif units < 500:
    bill = 800 + (units - 200) * 6
elif units < 800:
    bill = 800 + 1800 + (units - 500) * 8
else:
    bill = 800 + 1800 + 2400 + (units - 800) * 10
print("\nYour Electricity Bill for This Month is : ",bill)
print("\n","*"*40)
