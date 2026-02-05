from vpython import *
import time
"""credit: DotPhysics | while I modified or changed most lessons from this video
series, this is very similar, although not exactly, to the code he wrote"""

g1 = graph(xtitle="theta", ytitle ="range")
f1 = gcurve(color=color.blue)
def prange(ttheta, v0, r0):
    g = vector(0,-9.8,0)
    m = 0.05
    p = m*v0*vector(cos(ttheta), sin(ttheta), 0)
    t = 0
    dt = 0.001
    r=r0
    while r.y >= 0:
        F = m*g
        p += F*dt
        r += p*dt/m
        t += dt
    return(r.x)

theta = 1*pi/180
dtheta = 1*pi/180
vstart = 8

mrange = 0
mangle = 0

while theta < 89*pi/180:
    trange = prange(theta, vstart, vector(0,0,0))
    if trange > mrange:
        mrange = trange
        mangle = theta
    f1.plot(theta*180/pi, trange)
    theta += dtheta
print(str(mrange) + ' at ' + str(mangle*180/pi))
time.sleep(10)