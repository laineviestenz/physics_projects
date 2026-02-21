"""Rewriting the previous best angle to use matplotlib and numpy!"""
import matplotlib.pyplot as plt
import numpy as np
import math

def get_range(theta, velocity_i, mass, radius, initial_position=np.array([0,0,0])):
    """finds the distance an object travels (in the x direction), given an angle
    and initial velocity"""
    gravity = np.array([0,-9.8,0])
    pi = math.pi
    cross_area = pi*radius**2
    rho = 1.2
    drag_coefficient = 0.47
    momentum = mass*velocity_i*np.array([math.cos(theta*pi/180), math.sin(theta*pi/180), 0])
    position = initial_position
    height = initial_position[1]
    dt = 0.01
    while height >= 0:
        #calculate the net force vector using the quadratic drag formula
        Fnet = mass*gravity - 0.5*rho*cross_area*drag_coefficient*(np.linalg.norm(momentum/mass))**2*(momentum/np.linalg.norm(momentum))
        #the change in momentum equals force times change in time
        momentum = momentum + (Fnet * dt)
        #P/m = velocity; distance = velocity*time
        position = position + ((momentum/mass) * dt)
        height = position[1]
    return position[0]

def get_best_angle(velocity_i, mass, radius, initial_position=np.array([0,0,0])):
    """finds the angle that gives the furthest range"""
    angles = {}
    ranges = []
    i = 0
    dtheta = 0.1
    while i < 90:
        distance = float(get_range(i, velocity_i, mass, radius, initial_position))
        angles[distance] = i
        ranges.append(distance)
        i += dtheta
    max_range = max(ranges)
    best_angle = angles[max_range]
    return best_angle
    
def plot_best_angle(velocity_i, mass, radius, initial_position = np.array([0,0,0])):
    """graphs range vs angle (visualizes the get_best_angle() function)"""
    fig, graph = plt.subplots()
    x = []
    y = []
    angle = 0.1
    dtheta = 0.1
    while angle < 90:
        x.append(angle)
        y.append(get_range(angle, velocity_i, mass, radius, initial_position))
        angle += dtheta
    graph.plot(x,y)
    plt.show()

def plot_angle_by_velocity(max_velocity, mass, radius, initial_position=np.array([0,0,0])):
    """graphs the angle vs velocity. Notably, this returns a constant (+- the 
    numerical error) and is pretty slow. But it essentially shows that the
    best angle is independent of velocity."""
    fig, graph = plt.subplots()
    velocities = []
    angles = []
    velocity = 1
    dvelocity = 1
    while velocity <= max_velocity:
        velocities.append(velocity)
        angles.append(get_best_angle(velocity, mass, radius, initial_position))
        velocity += dvelocity
    graph.plot(velocities, angles)
    plt.show()

plot_angle_by_velocity(14, 5, 0.2)