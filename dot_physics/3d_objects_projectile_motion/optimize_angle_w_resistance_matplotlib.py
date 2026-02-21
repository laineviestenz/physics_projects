"""Rewriting the previous best angle to use matplotlib and numpy!"""
import matplotlib.pyplot as plt
import numpy as np
import math

def get_range(theta, velocity_i, mass, radius, initial_position=np.array([0,0,0])):
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

