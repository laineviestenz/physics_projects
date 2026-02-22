from vpython import *
import time
"""credit: DOT PHYSICS python tutorial"""

G = 6.67e-11
ME = 5.97e24
RE = 6.37e6

earth = sphere(pos=vector(0,0,0), radius=RE, texture=textures.earth)

craft = sphere(pos=vector(2*RE,0,0), radius=RE/30, color=color.yellow, make_trail=True)
craft.m = 1000
craft.p = vector(0,5500,0)*craft.m

t = 0
dt = 10

while t<100000:
    rate(200)
    r = craft.pos - earth.pos
    F = -G*ME*craft.m*norm(r)/mag(r)**2
    craft.p = craft.p + F*dt
    craft.pos = craft.pos + craft.p*dt/craft.m
    t += dt

time.sleep(10)