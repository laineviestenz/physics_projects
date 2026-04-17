"""The goal is to make a basic riemann sum function that will find the definite
integral of a function. The function will need to be input in the form of a
valid python equation with y as a function of x, though it might be good to add
a user interface that will convert latex or human readable text to python."""

"""notes:
add check for negative integral"""

"x**2+5x-3"
def riemann(equation, lower_bound, upper_bound, precision):
    dx = precision
    x = lower_bound
    total = 0
    while x < upper_bound:
        total += 0
        x += dx

def evaluate_function(function, value):
    """Helper function that will evaluate the fucntion at the input"""
    x = value
    return function

#this is good, the eval function will make this a lot easier
x = 1
print(eval('(x**2)+3*x-2'))