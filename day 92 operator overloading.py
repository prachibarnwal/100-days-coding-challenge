# add is for +
# sub is for -
# mul is for *
# truediv for /
# floordiv for //

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)
    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return Point(x, y)
    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Point(x,y)
    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return Point(x,y)


p1 = Point(5,7)
p2 = Point(2,4)

print("*"*32)
print("First Point is : ", p1)
print("Second Point is : ", p2)
print("*"*32)
print("Remainder : ", p1 % p2)
print("Sum : ", p1 + p2)
print("Difference : ", p1 - p2)
print("Product : ", p1 * p2)
print("Floor Division : ", p1 // p2)
print("Quotient : ", p1 / p2)
print("*"*32)
