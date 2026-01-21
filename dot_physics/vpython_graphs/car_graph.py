"""car A starts x = 0.5 m, v = 0.45
car B starts x = 0, v = 0, a = 0.2 m/s/s
note that this is a numerical approximation using an updated velocity at an increasingly
small interval, not an exact answer"""
from vpython import *
import time

g1 = graph()
f1 = gcurve(color = color.red,)
f2 = gcurve(color = color.blue)

#define start time t = 0
t = 0
#define step size
dt = 0.05

#define A parameters
xa = 0.5
va = 0.45

#define B parameters
xb = 0
vb = 0
ab = 0.2

while xa + 1 > xb:
    t += dt
    #find new A position
    xa += va * dt
    #find new B position
    vb += ab * dt
    xb += vb * dt
    f1.plot(t, xa)
    f2.plot(t, xb)
#keep graph open
time.sleep(15)