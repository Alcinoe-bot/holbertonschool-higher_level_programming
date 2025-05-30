#!/usr/bin/python3
"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    class verboselist
    """
    def append(self, item):
        """
        print when append is used
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """
        print when extend is used
        """
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """
        print when remove is used
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=-1):
        """
        print when pop is used
        """
        item = super().pop(item)
        print("Popped [{}] from the list.".format(item))
        return item
