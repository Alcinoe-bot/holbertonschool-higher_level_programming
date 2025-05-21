#!/usr/bin/python3
"""
module 2-square.py

size of area
"""


class Square:
    """
    create square class object

    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Initializes a square.

        Args:
        size (int): The size of the square. Must be >= 0.

        Raises:
           TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
