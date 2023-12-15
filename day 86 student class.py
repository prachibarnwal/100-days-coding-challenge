class Student:
    def __init__(self,rno,name,marks):
        self.rno = rno
        self.name = name
        self.marks = marks
        
    def input(self):
        self.rno = int(input("Enter Roll Number : "))
        self.name = input("Enter Name : ")
        self.marks = int(input("Enter Marks : "))

    def result(self):
        if self.marks >= 40:
            print(self.name," has Cleared the Exam")
        else:
            print(self.name," has not Cleared the Exam")

s1 = Student(10,"Parul",34)
s2 = Student(15,"Rahul",95)
#print(s1.name)
#print(s2.name)
print("   !!  Student 1  !!")
s1.input()
print("   !!  Student 2  !!")
s2.input()
print("-------Student 1-------")
s1.result()
print("-------Student 2-------")
s2.result()

    
