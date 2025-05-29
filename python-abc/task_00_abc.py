#!/usr/bin/env python3
"""
module task_00_abc
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    abstract class for animals
    """

    @abstractmethod
    def sound(self):
        """
        sound of animal
        """
        pass


class Dog(Animal):
    """
    subclass of animal
    """
    def sound(self):
        """
        sound of dog
        """
        return "Bark"


class Cat(Animal):
    """
    subclass of animal
    """
    def sound(self):
        """
        sound of cat
        """
        return "Meow"
