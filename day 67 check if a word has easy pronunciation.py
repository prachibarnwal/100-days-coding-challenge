word = input("Enter a Word : ")
c = 0
for ch in word:
    if ch.isalpha():
        if ch.lower() not in"aeiou":
            c += 1
            if c == 4:
                print("IT IS DIFFICULT TO PRONOUNCE")
                break
        else:
            c = 0
    else:
        print("INVALID INPUT")
        break
else:
    print("IT IS EASY TO PRONOUNCE")
