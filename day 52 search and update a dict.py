def create(d,n):
    for i in range(n):
        ename = input("Enter Enployee Name : ")
        sal = int(input("Enter Employee Salary : "))
        d[ename] = sal
def search(d,name):
    if name in d:
        print("Current Salary is : ",d[name])
        d[name] += d[name] * 1/4
        print("SALARY UPDATED........!!")
    else:
        print("No Employee Found With This Name")
d = {}
n = int(input("Enter How Many Employees Are There : "))
create(d,n)
print("Dictionary is : ",d)
name = input("Enter Employee Name whose Salary has to be Increased : ")
search(d,name)
print("Dictionary is : ",d)
