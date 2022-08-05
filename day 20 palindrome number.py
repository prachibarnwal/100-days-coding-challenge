num = int(input("Enter a Number to be Checked : "))
a = num
res = 0
while a > 0:
    d = a % 10
    res = res * 10 + d
    a //= 10

print("Reverse of ", num, " is ", res)
if num == res:
    print(num," is a Palindrome Number")
else:
    print(num," is not a Palindrome Number")




    
