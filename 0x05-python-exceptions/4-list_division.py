#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
            new_list.append(value)
        except (ZeroDivisionError, IndexError, TypeError) as e:
            if type(e) == ZeroDivisionError:
                print("division by 0")
            if type(e) == IndexError:
                print("out of range")
            if type(e) == TypeError:
                print("wrong type")
            new_list.append(0)
        finally:
            pass
    return (new_list)
