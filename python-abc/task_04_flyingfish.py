#!/usr/bin/env python3
"""
The Enigmatic FlyingFish
"""
from abc import ABC, abstractmethod


class Fish:
    """
    parent class for flyingfish
    """
    def swim(self):
        """
        fish is swiming
        """
        print("The fish is swimming")

    def habitat(self):
        """
        habitat fish
        """
        print("The fish lives in water")


class Bird:
    """
    class Bird
    """
    def fly(self):
        """
        bird fly
        """
        print("The bird is flying")

    def habitat(self):
        """
        habitat bird
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    class FlyingFish
    """
    def fly(self):
        """
        fly method
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        swim method
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        habitat method
        """
        print("The flying fish lives both in water and the sky!")
