n = input("Enter a String : ")
a = ''
for i in range(len(n)-1,-1,-1):
    a += n[i]

print("String is : ",n)
print("Reverse is : ",a)
if a == n:
    print("It is a Palindrome")
else:
    print("It's Not a Palindrome")
