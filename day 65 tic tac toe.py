import time
import random as rd
a = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    print("_"*12)
    for j in range(3):
        print("| ", a[i][j], end = ' ')
    print("|")
print("_"*12)

p1 = input("Enter Player's Name : ")
b = [1,2,3,4,5,6,7,8,9]
print("YOUR'RE PLAYING AGAINST COMPUTER.....BE CAREFUL !!")
turn = 1
while True:
    if turn % 2 == 1:
        pos = int(input(p1 + " enter the position for placing a X : "))
        b.remove(pos)
        for i in range(3):
            for j in range(3):
                if a[i][j] not in ("X","O") and a[i][j] == pos:
                    a[i][j] = 'X'
        turn += 1
    else:
        print("Turn Of Computer")
        pos = rd.choice(b)
        b.remove(pos)
        print("\nComputer Choses ",pos)
        for i in range(3):
            for j in range(3):
                if a[i][j] not in ("X","O") and a[i][j] == pos:
                    a[i][j] = 'O'
        turn += 1

        time.sleep(2)
        for i in range(3):
            print("_"*12)
            for j in range(3):
                print("|", a[i][j], end = ' ')
            print("|")
        print("_"*12)
        time.sleep(2)
        if a[0][0] == a[0][1] == a[0][2]:
            if a[0][0] == 'X':
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[1][0] == a[1][1] == a[1][2]:
            if a[1][0] == 'X':
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[2][0] == a[2][1] == a[2][2]:
            if a[2][2] == "X":
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[0][0] == a[1][0] == a[2][0]:
            if a[0][0] == "X":
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[0][1] == a[1][1] == a[2][1]:
            if a[1][1] == "X":
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[0][2] == a[1][2] == a[2][2]:
            if a[2][2] == "X":
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[0][0] == a[1][1] == a[2][2]:
            if a[0][0] == "X":
                print("COMPUTER WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif a[0][2] == a[1][1] == [2][0]:
            if a[0][2] == "X":
                print(p1, " WINS........!!!")
            else:
                print("COMPUTER WINS........!!!")
            break
        elif turn > 9:
            print("NOBODY WINS >_<")
            time.sleep(0.5)
            print("IT'S A DRAW")
                
            
