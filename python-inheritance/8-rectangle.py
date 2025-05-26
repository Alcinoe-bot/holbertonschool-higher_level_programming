#!/usr/bin/python3
"""
module 8-rectangle.py
"""


class BaseGeometry:
    """
    create BaseGeometry class object
    """

    def area(self):
        """
        area with exeption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value for integer and positive
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    create Rectangle class object
    """
    def __init__(self, width, height):
        """
        initialise rectangle
        """
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
