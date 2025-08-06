# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle: length × width"""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle: π × radius²"""
        return math.pi * (self.radius ** 2)
