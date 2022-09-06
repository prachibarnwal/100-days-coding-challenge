import random
import time

num = random.randint(1,100)
low = 1
high = 100
for i in range(5):
    guess = int(input("Enter Number Between " + str(low) + " to " + str(high) + " : "))
    time.sleep(1)
    if guess == num:
        print("*"*20)
        print("\t\tYOU WIN.........!!!!!!!")
        print("*"*20)
        break
    elif num > guess:
        print("\nSorry, but the number is Greater than your Guess \n")
        low = guess + 1
        time.sleep(1)
    elif num < guess:
        print("\nSorry, but the number is Lesser than your guess\n")
        high = guess - 1
        time.sleep(1)
else:
    print(">_<"*10)
    print("\t\tYOU LOOSE.........!!!!!")
    time.sleep(1)
    print("Ek number bhi guess nhi huaa terese......kya Gunda banega re tu xddd")
    time.sleep(3)
    print(num, " tha vo number.......HUFFF")
    print("~"*29)
