"""a ball is launched from the top of a hill that slopes downward (uniformily) at an angle phi
from the horizontal. What angle theta above the horizon should a ball be launched to maximize
its range?"""

import math

def get_range (vi, phi, theta, dx=0.01):
    height=0
    x=0
    
    while height > depth #make while ball above ground
        #calculate the depth of the ground at a point
        depth = -1*x*math.tan(phi)
        #calculate the height of the ball
            #kinematic equation here
        x += dx
    return x

def optimize_angle (dtheta=0.1):
    phi=10
    theta=0
    while theta < 90:
        pass

