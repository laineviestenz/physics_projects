from vpython import *
import time

def prange(ttheta, v0, r0):
    g = vector(0,-9.8,0)
    m = 0.05
    p = m*v0*vector(cos(ttheta), sin(ttheta), 0)
    t = 0
    dt = 0.001
    while r.y >= 0:
        F = m*g
        p += F*dt
        r += p*dt/m
        t += dt
    return(r,x)
print("range = " + str(r.x), ' m')
time.sleep(10)