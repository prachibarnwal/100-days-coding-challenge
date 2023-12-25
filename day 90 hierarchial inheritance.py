class Employee():
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def display(self):
        print("\n")
        print("Employee I'd is : ", self.eid)
        print("Name is : ", self.name)
        print("Salary is : ", self.salary)
        print("\n")

class Worker(Employee):
    def __init__(self, eid, name, salary, overtime_hrs):
        self.overtime_hrs = overtime_hrs
        super().__init__(eid, name, salary)

    def displayInfo(self):
        print("\n")
        super().display()
        print("Overtime Hours Worked : ", self.overtime_hrs)
        print("Overtime Earned is : ", self.overtime_hrs * 50)
        print("\n")

class Salesman(Employee):
    def __init__(self, eid, name, salary, sales):
        self.sales = sales
        super().__init__(eid, name, salary)
    def displayInfo(self):
        print("\n")
        super().display()
        print("Monthly Sales : ",self.sales)
        print("Commission Earned is : ", self.sales * 10/100)
        print("\n")

while True:
    print("Press 1 : Fetch the Details of an Employee")
    print("Press 2 : Fetch the Details of a Worker")
    print("Press 3 : Fetch the Details of a Salesman")
    print("Press 4 : Exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        n = input('Enter Employee Name : ')
        e = int(input("Enter Employee's I'd : "))
        s = int(input("Enter Employee's Salary : "))
        emp = Employee(e, n, s)
        emp.display()
    elif ch == 2:
        n = input('Enter Worker Name : ')
        e = int(input("Enter Worker's I'd : "))
        s = int(input("Enter Worker's Salary : "))
        h = int(input("Enter Worker's Overtime Hours : "))
        w = Worker(e, n, s, h)
        w.displayInfo()
    elif ch == 3:
        n = input('Enter Salesman Name : ')
        e = int(input("Enter Salesman's I'd : "))
        s = int(input("Enter Salesman's Salary : "))
        h = int(input("Enter Sales of Salesman : "))
        s = Salesman(e, n, s, h)
        s.displayInfo()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")
        break
