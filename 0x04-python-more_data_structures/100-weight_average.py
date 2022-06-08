#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score = sum([i[0] * i[1] for i in my_list])
    weight = sum([i[1] for i in my_list])
    result = score / weight
    return result
