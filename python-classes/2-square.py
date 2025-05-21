#!/usr/bin/python3
"""
module 2-square.py

taille de l'area
"""


class Square:
    """
    créer une classe objet carré

    """
    def __init__(self, size=0):
        """
        size du carré

        vérifie s'il les valeurs sont bien des integer
        ou supérieur à 0 sinon erreur

        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
