def plus(a: int | float, b: int | float):
    return float(a) + float(b)

def minus(a: int | float, b: int | float):
    return float(a) - float(b)

def multiply(a: int | float, b: int | float):
    return float(a) * float(b)

def divide(a: int | float, b: int | float):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "ERROR!!! You are trying to divide a number by zero, please enter it again"