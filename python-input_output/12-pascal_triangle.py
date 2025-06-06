#!/usr/bin/python3
"""
Module 12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    triangle
    """
    Triangle = []
    lineP = []
    for i in range(n):
        line = [1] + [sum(lineP[elt:elt + 2]) for elt in range(len(lineP) - 1)]
        if i > 0:
            line = line + [1]
        Triangle.append(line)
        lineP =  line
    return Triangle
