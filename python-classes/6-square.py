#!/usr/bin/python3
"""
module 6-square.py

final program for Square
"""


class Square:
    """
    create square class object
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        size of square
        """
        return self.__size

    @property
    def position(self):
        """
        get position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets position
        he must be a tuple of positive integers
        Raise:
            TypeError
            ValueError
        """
        if (type(value) is not tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if (self.size == 0):
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
