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
d = 3.7 #m above spring
k = 0.15*10**6 #N/m
F_friction = 4400 #N

def get_impact_speed (m, d, F_friction, dx = 0.05):
    initial_energy = m * 9.8 * d
    v = math.sqrt((initial_energy + (F_friction * d)/ (0.5 * m)))
    print (v)

get_impact_speed(m, d, F_friction)