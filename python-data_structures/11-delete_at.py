#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0 or idx >= len(my_list)):
        my_List = my_list.copy()
        return (my_List)
    del my_list[idx]
    my_List = my_list.copy()
    return (my_List)
