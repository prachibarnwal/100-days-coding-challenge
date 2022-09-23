txt = input("Enter a String : ")
c = 0
for ch in txt:
    if ch.lower() in 'aeiou':
        c += 1
print("Number of Vowels are : ",c)
