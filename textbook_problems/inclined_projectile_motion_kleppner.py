"""a ball is launched from the top of a hill that slopes downward (uniformily) at an angle phi
from the horizontal. What angle theta above the horizon should a ball be launched to maximize
its range?"""

import math

def get_range (vi, phi, theta, dx=0.01):
    height=0
    horizontal_distance = 0
    depth=0
    t=0
    
    while height >= depth: #make while ball above ground
        #calculate how far the ball has traveled horizontally
        horizontal_distance = vi*math.cos(theta)*t
        #calculate the depth below the horizon at the horizontal distance
        depth = -1*horizontal_distance*math.tan(phi)
        #calculate the height of the ball
        height = vi*math.sin(theta)*t - (0.5 * 9.8 * t**2)
        print(horizontal_distance, depth, height)
        #increment time
        t += dx    
    return t

print(get_range(10, 10, 30))