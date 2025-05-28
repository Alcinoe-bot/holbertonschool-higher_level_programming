#!/usr/bin/python3
"""
module 10-rectangle.py
"""


Rectangle = __import__('9-rectangle').Rectangle


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
