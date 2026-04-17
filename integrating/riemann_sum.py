"""The goal is to make a basic riemann sum function that will find the definite
integral of a function. The function will need to be input in the form of a
valid python equation with y as a function of x, though it might be good to add
a user interface that will convert latex or human readable text to python."""

"""notes:
add check for negative integral"""

"x**2+5x-3"
def riemann(function, lower_bound, upper_bound, precision):
    dx = precision
    #assumes a center sum for now
    x = lower_bound + (dx/2)
    total = 0
    while x < upper_bound:
        total += (eval(function)*dx)
        x += dx
    return total

print(riemann("x**2", 0, 1, 0.001))