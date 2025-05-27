#!/usr/bin/python3
"""
module 1-my_list.py
"""


class MyList(list):
    """
    create class
    """
    def print_sorted(self):
        """
        print list
        """
        print(sorted(self))
