import random
import time

name1 = input("Enter First Player's Name : ")
name2 = input("Enter Second Player's Name : ")
print("Fetching Names..........!!!")
time.sleep(3)

val1 = random.randint(1,6)
val2 = random.randint(1,6)

print("Player 1 got ", val1)
time.sleep(2)
print("Player 2 got ", val2)
time.sleep(2)

if val1 > val2:
    print(name1, " WINS......!!!!")
elif val2 > val1:
    print(name2, " WINS......!!!!")
else:
    print("NOBODY WINS....IT'S A DRAW >__<")
