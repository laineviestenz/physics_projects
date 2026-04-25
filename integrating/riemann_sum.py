"""The goal is to make a basic riemann sum function that will find the definite
integral of a function. The function will need to be input in the form of a
valid python equation with y as a function of x, though it might be good to add
a user interface that will convert latex or human readable text to python."""

"""There is a few bugs in the graphing and visualization part, first it only
works when the lowerbound is zero because of the way that the list is indexed,
and there is currently a bug that prevents it from running at all"""
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
        while x <= (upper_bound-dx):
            plt.bar(x, eval(function), dx, align = 'edge')
            total += dx * eval(function)
            x+=dx
#begin graphing function
    c = [i for i in range(lower_bound, upper_bound, dx)]
    d = []
    
    for i in range (lower_bound, upper_bound, dx):
        x=i
        d.append(eval(function))
    plt.plot(c, d)
    plt.show()
    
#     elif type.lower() == 'right' or type.lower() == 'r':
#         x = lower_bound + dx
#         while x <= upper_bound:
#             total += eval(function)*dx
#             x += dx
#         print('the right sum is: ', total * negative)
       
#         #begin graphing function
#         fig, ax = plt.subplots()
#         c = [i for i in range(lower_bound+dx, upper_bound, dx)]
#         d = []
        
#         for i in range (lower_bound+dx, upper_bound, dx):
#             x=i
#             d.append(eval(function))
#             print(d)
#         plt.plot(c,d)
#         for x in range(lower_bound + dx, upper_bound, dx):
#             print(x)
#             plt.bar(x-dx, d[x-1], dx, align='edge')
#         plt.show()
    

#     else:
#         x = lower_bound + (dx*0.5)
#         while x <= upper_bound - (dx*0.5):
#             total += eval(function)*dx
#             x += dx
#         print('the center sum is: ', total * negative)
#         #begin graphing function
#         fig, ax = plt.subplots()
#         c = [i for i in range(lower_bound, upper_bound, dx)]
#         d = []
        
#         for i in range (lower_bound, upper_bound, dx):
#             x=i+0.5*dx
#             d.append(eval(function))
        
#         plt.plot(c,d)
#         for x in range(lower_bound, upper_bound):
#             plt.bar(x, d[x], dx, align='center')
#         plt.show()
riemann("x**2", 0, 10, 1, type='left')