#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_list = 0
    if (my_list):
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
                nb_list += 1
            except IndexError:
                print()
                return (nb_list)
    print()
    return (nb_list)
