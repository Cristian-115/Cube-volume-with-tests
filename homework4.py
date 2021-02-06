
from logging import StringTemplateStyle, raiseExceptions


def cube_volume(edge):
    if edge <= 0:
        raise Exception("number must be positive")
    elif not type(edge) is float:
        raise TypeError("number must be a float")
    
    return edge * edge * edge

def fname(first, last):
    if not type(first) is str:
        raise TypeError("first name must be a string")
    elif not type(last) is str:
        raise TypeError("last name must be a string")
    return str(first) + " " +  str(last)

def avg(list1):
    if not type(list1) is list:
        raise TypeError("must pass in a list")
    average = sum(list1) / len(list1)
    return average


