from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Main Program
circle = Circle(7)
rectangle = Rectangle(10, 5)

print("Circle Area =", round(circle.area(), 2))
print("Rectangle Area =", rectangle.area())