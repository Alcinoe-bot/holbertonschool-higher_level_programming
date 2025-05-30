#!/usr/bin/python3
"""
class Shapes, Interfaces, and Duck Typing
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    area and perimeter
    """
    @abstractmethod
    def area(self):
        """
        area of shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter of shape
        """
        pass


class Circle(Shape):
    """
    class circle
    """
    def __init__(self, radius):
        """
        initialize circle
        """
        self.radius = radius

    def area(self):
        """
        area of circle
        """
        return pi * (self.radius * self.radius)

    def perimeter(self):
        """
        perimeter of circle
        """
        return abs((2 * self.radius) * pi)


class Rectangle(Shape):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
        initialize rectangle
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        area of rentangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter of rectangle
        """
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """
    give information about area and perimeter
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
