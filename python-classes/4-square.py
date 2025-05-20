#!/usr/bin/python3
class Square:
    """
    créer une classe objet carré
    """
    def __init__(self, size=0):
        self.__size = size
    """
    initialise le carré
    """
    @property
    def size(self):
        return self.__size
    """
    taille du carré
    """
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    size du carré

    vérifie s'il les valeurs sont bien des integer
    ou supérieur à 0 sinon erreur

    """
    def area(self):
        return (self.__size**2)
    """
    return le carré de la taille du carré
    """
