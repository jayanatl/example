# Class Circle
class Circle():
    def __init__(self, r):
        self.radius = r
        self.pi = 3.14

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

    perimeter = circumference

    def __repr__(self):
        return f"Circle(r={self.radius})"


# Class Rectangle
class Rectangle():
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def is_square(self):
        return true if self.length == self.breadth else false

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def __repr__(self):
        return f"Rectangle(l={self.length}, b={self.breadth})"
