#!/usr/bin/python3
"""
module 10-rectangle.py
"""


Rectangle = __import__('10-square').Rectangle


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

    def __str__(self):
        """
        string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
