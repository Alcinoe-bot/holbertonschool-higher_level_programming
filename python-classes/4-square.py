#!/usr/bin/python3
"""
module 4-square.py

definees a Square class by its size area and private attribute
"""


class Square:
    """
    create square class object
    """
    def __init__(self, size=0):
        """
        Initializes a square.
        """
        self.__size = size

    @property
    def size(self):
        """
        size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initializes a square.

        Args:
        value: The size of the square. Must be >= 0.

        Raises:
           TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        return area of square
        """
        return (self.__size**2)
