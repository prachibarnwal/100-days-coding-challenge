import pickle

eid = int(input("Enter Employee Id : "))
name = input("Enter Employee Name : ")
salary = int(input("Enter Employee Salary : "))
data = [eid,name,salary]

f = open("employ.dat","ab")

pickle.dump(data,f)
f.close()
print("ADDED")
