#!/usr/bin/python3
"""
module 10-rectangle.py
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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        initialise square by size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
