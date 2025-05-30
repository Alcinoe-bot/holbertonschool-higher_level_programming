#!/usr/bin/python3
"""
CountedIterator
"""
from abc import ABC, abstractmethod


class CountedIterator:
    """
    Keeping Track of Iteration
    """
    def __init__(self, Iterable):
        """
        initialize countiterator
        """
        self.iterator = iter(Iterable)
        self.counter = 0

    def get_count(self):
        """
        print the number of items that have been fetched
        """
        return self.counter

    def __next__(self):
        """
        increment the counter each time the __next__
        method is called
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        a valid iterable in Python
        """
        return self
