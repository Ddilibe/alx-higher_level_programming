#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a = change_one(tuple_a)
    if len(tuple_b) == 1:
        tuple_b = change_one(tuple_b)
    if len(tuple_a) == 0:
        tuple_a = change_two(tuple_a)
    if len(tuple_b) == 0:
        tuple_b = change_two(tuple_b)
    f = []
    for i in range(0, 2):
        f.append(tuple_a[i] + tuple_b[i])
    return (tuple(f))

def change_one(tupl):
    tupl = list(tupl)
    tupl.append(0)
    tupl = tuple(tupl)
    return (tupl)

def change_two(tupl):
    tupl = list(tupl)
    for i in range(0,2):
        tupl.append(0)
    tupl = tuple(tupl)
    return (tupl)
