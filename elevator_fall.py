"""
The cable of the 1800 kg elevator cab in Fig. 8-59 snaps when the cab is at
rest at the first floor, where the cab bottom is a distance d = 3.7 m above a 
spring of spring constant k = 0.15 MN/m. A safety device clamps the cab against 
guide rails so that a constant frictional force of 4.4 kN opposes the cab's
motion.
(a) Find the speed of the cab just before it hits the spring.
(b) Find the maximum distance x that the spring is compressed (the frictional force still acts during this compression).
(c) Find the distance that the cab will bounce back up the shaft.
(d) Using conservation of energy, find the approximate total distance that the cab will move before coming to rest. (Assume that the frictional force on the cab is negligible when the cab is stationary.)
"""
import math
m = 1800 #kg
d_i = 3.7 #m above spring
k = 0.15*10**6 #N/m
F_friction = 4400 #N
g = 9.8 #m/s^2
v_i = 0
x_i = 0

def get_gpe (m, d):
    return (m * g * d)

def get_ke (m, v):
    return (0.5 * m * v**2)

def convert_ke_to_velocity (m, d, k, F_friction):
    pass

def get_epe (m, x, k):
    return (0.5 * k * x**2)

def create_graph (m, d, k, F_friction):
    """Create a graph with total energy, KE, EPE, GPE, and velocity"""
    pass

def get_total_energy (m, d, k, v, x):
    """requires velocity and spring displacement to be calculated first"""
    E = get_gpe(m, d) + get_ke(m, v) + get_epe(m, x, k)
    return E

def update_pos_vel(m, g, x_i, t):
    #total energy = gpe + ke + epe
    #

#calculate the initial energy
E_i = get_total_energy(m, d_i, k, v_i, x_i)



