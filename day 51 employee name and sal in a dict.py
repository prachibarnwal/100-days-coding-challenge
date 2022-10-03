def create(d,n):
    for i in range(n):
        ename = input("Enter Enployee Name : ")
        sal = int(input("Enter Employee Salary : "))
        job = input("Enter Job : ")
        d[ename] = [sal,job]
d = {}
n = int(input("Enter How Many Employees Are There : "))
create(d,n)
print("Dictionary is : ",d)
