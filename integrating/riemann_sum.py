"""The goal is to make a basic riemann sum function that will find the definite
integral of a function. The function will need to be input in the form of a
valid python equation with y as a function of x, though it might be good to add
a user interface that will convert latex or human readable text to python."""

import math
import matplotlib.pyplot as plt

def riemann(function, lower_bound, upper_bound, precision, type = 'center'):
    dx = precision
    total = 0
    negative = 1
    #check reverse integral
    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
        negative = -1

    if type.lower() == 'left' or type.lower() == 'l':
        x = lower_bound
        while x <= upper_bound - dx:
            total += eval(function)*dx
            x += dx
        print('the left sum is: ', total * negative)
    
    elif type.lower() == 'right' or type.lower() == 'r':
        x = lower_bound + dx
        while x <= upper_bound:
            total += eval(function)*dx
            x += dx
        print('the right sum is: ', total * negative)
    
    else:
        x = lower_bound + (dx*0.5)
        while x <= upper_bound - (dx*0.5):
            total += eval(function)*dx
            x += dx
        print('the center sum is: ', total * negative)

riemann("x**2", 0, 10, 1, type='left')
riemann("x**2", 0, 10, 1, type='center')
riemann("x**2", 0, 10, 1, type='right')