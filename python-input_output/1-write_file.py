#!/usr/bin/python3
"""
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(text))
