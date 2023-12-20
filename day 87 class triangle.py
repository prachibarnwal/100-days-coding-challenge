class Triangle:
    def __init__(self,x,y,z):
        self.s1 = x
        self.s2 = y
        self.s3 = z
    def input(self):
        self.s1 = int(input("Enter Side 1 : "))
        self.s2 = int(input("Enter Side 2 : "))
        self.s3 = int(input("Enter Side 3 : "))
    def show(self):
        print("Side 1 is : ",self.s1)
        print("Side 2 is : ",self.s2)
        print("Side 3 is : ",self.s3)

t1 = Triangle(3,8,4)
t2 = Triangle(9,2,4)
print("*******Triangle 1*******")
t1.input()
print("*******Triangle 2*******")
t2.input()
print("_____Triangle 1_____")
t1.show()
print("_____Triangle 2_____")
t2.show()
