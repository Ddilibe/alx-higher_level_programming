#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = list(list(list(text)))
    add_text = []
    going_to = []
    for i in new_text:
        if len(going_to) == 0 and i in (" ", "  ", "        "):
            continue
        if i in ('.', '?', ':'):
            going_to.append(i)
            going_to = "".join(going_to)
            add_text.append(str(going_to))
            going_to = []
            continue
        going_to.append(i)
    going_to = "".join(going_to)
    add_text.append(str(going_to))
    going_to = []
    for i in add_text:
        print("{}\n".format(i))

