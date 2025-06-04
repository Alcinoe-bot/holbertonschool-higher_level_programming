#!/usr/bin/python3
"""
class Student
"""


class Student:
    """
    class
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        print dictionary
        """
        if (isinstance(attrs, list) and all(isinstance(i, str) for i in attrs)):
            result = {}
            for (i, j) in self.__dict__.items():
                if i in attrs:
                    result[i] = j
            return result
        else :
            return self.__dict__
