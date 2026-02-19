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
    momentum = mass*np.array([math.cos(theta), math.sin(theta), 0])
    y = 1
    while y > 0:
        Fnet = mass*gravity - 0.5*rho*cross_area*drag_coefficient*(np.linalg.norm(momentum/mass))**2*(momentum/np.linalg.norm(momentum))

