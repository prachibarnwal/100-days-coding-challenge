# gt for greater than
# lt for less than
# eq for equal to

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def __str__(self):
        return "Length {0}, Breadth {1})".format(self.l, self.b)
    def __gt__(self, other):
        if (self.l * self.b) > (other.l * other.b):
            return True
        else:
            return False

r1 = Rectangle(10, 12)
r2 = Rectangle(12,17)
print("First Rectangle is : ", r1)
print("Second Rectangle is : ", r2)
if r1 > r2:
    print("First Rectangle is Bigger in Area ")
else:
    print("Second Rectangle is Bigger in Area")
