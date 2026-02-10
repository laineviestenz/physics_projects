""" A rock is thrown upward from level ground in such a way that the maximum
height of its flight is equal to its horizontal range R. 
a) what is the angle, theta, which the rock is thrown at? """

import math

def get_angle(vi, dtheta = 0.0001*math.pi/180):
    theta = 1*math.pi/180
    height = (vi**2 * math.sin(theta)**2/(2*9.8))
    distance = vi**2 * (math.sin(2*theta)) / (9.8)
    
    while theta < math.pi/2:
        height = (vi**2 * math.sin(theta)**2/(2*9.8))
        distance = vi**2 * (math.sin(2*theta)) / (9.8)
        if abs(distance - height) < .1:
            return theta*180/math.pi
        theta += dtheta

print(get_angle(150))