# single level inheritance
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name is : ", self.name)
        print("Age is : ", self.age)

class Student(Person):
    def __init__(self, name, age, dob):
        self.dob = dob
        super().__init__(name, age)

    def displayInfo(self):
        print(self.name, "\t", self.age, '\t', self.dob)

stu = Student("Mayank", 19, "19-12-2004")
stu.display()
print("\n")
stu.displayInfo()
