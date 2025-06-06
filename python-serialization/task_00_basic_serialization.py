#!/usr/bin/env python3
"""
Module task_00_basic_serialization.py
"""


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
    pass


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r') as openfile:
        return json.load(openfile)
    pass
