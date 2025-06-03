#!/usr/bin/python3
"""
Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Object to a text file, using a JSON representation
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
