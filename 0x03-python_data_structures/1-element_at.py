#!/usr/bin/python3
def element_at(my_list, idx):
    if not(idx >= 0):
        return None
    else:
        if not((idx ) < len(my_list)):
            return None
        else:
            return my_list[idx]
