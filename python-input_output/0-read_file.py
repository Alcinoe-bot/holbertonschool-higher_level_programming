#!/usr/bin/python3
"""
read a file
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
