#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elt in matrix:
        for number in elt:
            print("{:d}".format(number), end='')
            if (number is not elt[len(elt) - 1]):
                print(" ", end='')
        print()
