from vpython import *
import time

def get_range(angle, v0, initial_position):
    """run until the ball reaches zero, and return the position(range of the ball)"""
    g = vector(0,-9.8,0)
    mass = 0.05
    radius = 0.2
    rho = 1.2
    cross_area = pi*radius**2
    drag_coef = 0.47
    momentum = mass*v0*vector(cos(angle), sin(angle), 0)
    dt = 0.001
    position=initial_position
    while position.y >= 0:
        force = mass*g - 0.5*rho*cross_area*drag_coef*mag(momentum/mass)**2*norm(momentum)
        momentum += force*dt
        position += momentum*dt/mass
    return(position.x)

def plot_best_angle(v0, initial_position):
    #initialize the graph and curve
    g1 = graph(xtitle="theta", ytitle ="range")
    f1 = gcurve(color=color.blue)
    theta = 0*pi/180
    dtheta = 1*pi/180

    while theta < 89*pi/180:
        trange = get_range(theta, v0, initial_position)
        f1.plot(theta*180/pi, trange)
        theta += dtheta

def get_best_angle(v0, initial_position):
    theta = 0*pi/180
    dtheta = 1*pi/180

    maxrange = 0
    maxangle = 0

    while theta < 89*pi/180:
        trange = get_range(theta, v0, initial_position)
        if trange > maxrange:
            maxrange = trange
            maxangle = theta
        theta += dtheta
    print(str(maxrange) + ' at ' + str(maxangle*180/pi))


get_best_angle(12, vector(0,0,0))
plot_best_angle(12, vector(0,0,0))
time.sleep(10)
