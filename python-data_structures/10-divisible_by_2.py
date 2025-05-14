#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_List = []
    for i in my_list:
        if i % 2 == 0:
            my_List.append(True)
        else:
            my_List.append(False)
    return (my_List)
