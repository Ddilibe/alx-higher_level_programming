#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return (0)
    arabic = []
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    nume = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    w = list(roman_string)
    for i in range(0, len(w)):
        if w[i].upper() in nume:
            if i+1 < len(w):
                if w[i].upper() == 'I':
                    if w[i+1].upper() == 'X':
                        put = -(roman.get(w[i].upper()))
                    elif w[i+1].upper() == 'V':
                        put = -(roman.get(w[i].upper()))
                    else:
                        put = roman.get(w[i].upper())
                elif w[i].upper() == 'X':
                    if w[i+1].upper() == 'L':
                        put = -(roman.get(w[i].upper()))
                    elif w[i+1].upper() == 'C':
                        put = -(roman.get(w[i].upper()))
                    else:
                        put = roman.get(w[i].upper())
                elif w[i].upper() == 'C':
                    if w[i+1].upper() == 'M':
                        put = -(roman.get(w[i].upper()))
                    elif w[i+1].upper() == 'D':
                        put = -(roman.get(w[i].upper()))
                    else:
                        put = roman.get(w[i].upper())
                else:
                    put = roman.get(w[i].upper())
            else:
                put = roman.get(w[i].upper())
            arabic.append(put)
        else:
            return (0)
    result = sum(arabic)
    return (result)
