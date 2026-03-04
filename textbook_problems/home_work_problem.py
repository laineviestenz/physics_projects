""" A rock is thrown upward from level ground in such a way that the maximum
height of its flight is equal to its horizontal range R. 
a) what is the angle, theta, which the rock is thrown at? """

import math
import matplotlib.pyplot as plt

def get_angle(vi, dtheta = 0.1*math.pi/180):
    """returns the angle at which height and distance are the same
    (within 1%)"""
    #initial theta = 1 degree
    theta = 1*math.pi/180
    
    while theta < math.pi/2:
        """cycle through the angles starting a 1 degree, stop at 90 degrees if
        the angle is not found. This may result in an infinite loop - something
        to fix in the future."""
        #calculate height and distance given vi and theta
        height = (vi**2 * math.sin(theta)**2/(2*9.8))
        distance = (vi*math.cos(theta)*2*vi*math.sin(theta))/9.8
        #if the distance and height are within 1%, return the angle theta
        if abs(distance - height)/distance < 0.01:
            return theta*180/math.pi
        #increment theta
        theta += dtheta

def graph_anglevspeed(maxvelocity, dv=0.5):
    """prints a graph of angle vs initial velocity, takes maxvelocity parameter
    to set the domain of the graph, and dv to set the resolution (this shows 
    that the angle is the same regardless of the initial velocity)"""
    #configure graph
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.set_ylabel('angle')
    ax.set_xlabel('initial velocity')
    #set initial velocity and create lists for angles and velocities to be stored in
    vi = 1
    angles = []
    velocities = []
    while vi < maxvelocity:
        """append angle and velocity, incrementing by dv until reaching the set
        max velocity"""
        angles.append(get_angle(vi))
        velocities.append(vi)
        vi += dv
    #plot the values
    ax.plot(velocities, angles)
    plt.show()
#creates a graph with 1-150 m/s initial velocity
graph_anglevspeed(150)