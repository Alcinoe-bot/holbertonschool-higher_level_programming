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

    def to_json(self):
        """
        print dictionary
        """
        return self.__dict__
