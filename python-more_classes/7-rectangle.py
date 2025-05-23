#!/usr/bin/python3
"""
module 7-rectangle.py

class for rectangle
"""


class Rectangle:
    """
    create rectangle class object
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        width of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width of rectangle
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height of rectangle
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return perimeter of rentangle
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        modifies str object
        visible for humans
        """
        if not self.perimeter():
            return ""
        return ('\n'.join("{}".format(self.print_symbol) * self.width
                          for i in range(self.height)))

    def __repr__(self):
        """
        modifies repr object
        visible like informations
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        modifies del object
        """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
