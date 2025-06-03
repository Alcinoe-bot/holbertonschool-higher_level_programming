#!/usr/bin/python3
"""
writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    lines = 0
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in f:
            lines += 1
        return lines
