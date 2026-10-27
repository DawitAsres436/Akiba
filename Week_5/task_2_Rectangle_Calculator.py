class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)

    def __str__(self):
        return f"Rectangle(Length = {self.length}, width = {self.width})"

Rectangel1 = Rectangle(8, 6)
Rectangel2 = Rectangle(5, 4)

print(Rectangel1)
print(f"Area:{Rectangel1.area()}")
print(f"Perimeter:{Rectangel1.perimeter()}")
print("-"*40)
print(Rectangel2)
print(f"Area:{Rectangel2.area()}")
print(f"Perimeter:{Rectangel2.perimeter()}")


    