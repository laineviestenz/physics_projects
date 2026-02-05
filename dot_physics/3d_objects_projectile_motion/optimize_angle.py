from vpython import *
import time
"""credit: DotPhysics | while I modified or changed most lessons from this video
series, this is very similar, although not exactly, to the code he wrote"""

def get_range(angle, v0, initial_position):
    """run until the ball reaches zero, and return the position(range of the ball)"""
    g = vector(0,-9.8,0)
    mass = 0.05
    momentum = mass*v0*vector(cos(angle), sin(angle), 0)
    dt = 0.001
    position=initial_position
    while position.y >= 0:
        force = mass*g
        momentum += force*dt
        position += momentum*dt/mass
    return(position.x)

def plot_best_angle():
    #initialize the graph and curve
    g1 = graph(xtitle="theta", ytitle ="range")
    f1 = gcurve(color=color.blue)
    theta = 0*pi/180
    dtheta = 1*pi/180
    v0 = 8

    while theta < 89*pi/180:
        trange = get_range(theta, v0, vector(0,0,0))
        f1.plot(theta*180/pi, trange)
        theta += dtheta

def get_best_angle():
    theta = 0*pi/180
    dtheta = 1*pi/180
    v0 = 8

    maxrange = 0
    maxangle = 0

    while theta < 89*pi/180:
        trange = get_range(theta, v0, vector(0,0,0))
        if trange > maxrange:
            maxrange = trange
            maxangle = theta
        theta += dtheta
    print(str(maxrange) + ' at ' + str(maxangle*180/pi))


get_best_angle()
plot_best_angle()
time.sleep(10)
