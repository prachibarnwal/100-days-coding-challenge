f = open("STORY.txt","w")
f.write("This is a Sample File which we are creating using a Python Program.\n")
f.write("This file will be used through another program to process its data.\n")
f.write("Thankyou")
f.close()

f = open("STORY.txt","r")
data = f.read()
print(data)

vowels = 0
for ch in data:
    if ch in"AEIOUaeiou":
        vowels += 1
print("NUMBER OF VOWELS IS : ",vowels)
f.close()
