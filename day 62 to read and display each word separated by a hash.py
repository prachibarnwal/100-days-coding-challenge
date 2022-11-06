f = open("STORY.txt","r")
data = f.readlines()
for ch in data:
    for word in ch.split():
        print(word,end = "#")
    print()
f.close()
