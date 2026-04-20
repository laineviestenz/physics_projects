"""The goal is to make a basic riemann sum function that will find the definite
integral of a function. The function will need to be input in the form of a
valid python equation with y as a function of x, though it might be good to add
a user interface that will convert latex or human readable text to python."""

import math
def riemann(function, lower_bound, upper_bound, precision, type = 'center'):
    negative = 1
    dx = precision
    #check reverse integral
    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
        negative = -1
    
    #assumes a center sum for now
    x = lower_bound + (dx/2)
    if type.lower() == 'left':
        x = lower_bound
    elif type.lower() == 'right':
        x = lower_bound + dx
        total = 0
        while x < upper_bound:
            y = eval(function)*dx
            total += y
            print('right', x, (eval(function)*dx), total)
            x += dx
        return total * negative
    
    total = 0
    while x < upper_bound and not type.lower() == 'right':
        y = eval(function)*dx
        total += y
        print(x, (eval(function)*dx), total)
        x += dx
    return total * negative

print(riemann("x**2", 0, 10, 1, type='right'))