#!/usr/bin/python3
def convert_roman(ch):
    """
    converts a roman numeral character into the respective integer
    """
    ret = -1
    if ch == 'I':
        ret = 1
    elif ch == 'V':
        ret = 5
    elif ch == 'X':
        ret = 10
    elif ch == 'L':
        ret = 50
    elif ch == 'C':
        ret = 100
    elif ch == 'D':
        ret = 500
    elif ch == 'M':
        ret = 1000
    return ret
