#!/usr/bin/python3
"""
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    returns the number of characters written
    """
    lines = 0
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in f:
            lines += 1
    return lines
