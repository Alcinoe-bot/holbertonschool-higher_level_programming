#!/usr/bin/env python3

from abc import ABC, abstractmethod


class SwimMixin:
    """
    First mixinclass
    """

    def swim(self):
        pass

    def fly(self):
        pass

    def name(self):
        pass


class FlyMixin:
    """
    First mixinclass
    """

    def swim(self):
        pass

    def fly(self):
        pass

    def name(self):
        pass


class Dragon (SwimMixin, FlyMixin):
    """
    A Dragon named nounours
    """
    def swim(self):
        print("The creature swims!")

    def fly(self):
        print("The creature flies!")

    def roar(self):
        print("The dragon roars!")

    def name(self):
        print("I'm a cute Dragon and my name is nounours!")
