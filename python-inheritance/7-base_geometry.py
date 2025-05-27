#!/usr/bin/python3
"""
module 7-base_geometry.py
"""


class BaseGeometry:
    """
    create BaseGeometry class object
    """
    def __init__(self):
        """
        initialise class
        """
        pass

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
