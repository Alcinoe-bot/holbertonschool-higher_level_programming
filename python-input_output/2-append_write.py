#!/usr/bin/python3
"""
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    returns the number of characters added
    """
    with open(filename, mode='a+', encoding='utf-8') as file:
        return (file.write(text))
