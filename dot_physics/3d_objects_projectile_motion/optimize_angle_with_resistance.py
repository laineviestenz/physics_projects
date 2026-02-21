from vpython import *
import time

def get_range(angle, v0, initial_position, mass, radius):
    """run until the ball reaches zero, and return the position(range of the ball)"""
    g = vector(0,-9.8,0)
    rho = 1.2
    cross_area = pi*radius**2
    drag_coef = 0.47
    momentum = mass*v0*vector(cos(angle), sin(angle), 0)
    dt = 0.001
    position=vector(initial_position.x, initial_position.y, initial_position.z)
    while position.y >= 0:
        force = mass*g - 0.5*rho*cross_area*drag_coef*mag(momentum/mass)**2*norm(momentum)
        momentum += force*dt
        position += momentum*dt/mass
    return(position.x)

def plot_best_angle(v0, initial_position, mass, radius):
    #initialize the graph and curve
    g1 = graph(xtitle="theta", ytitle ="range")
    f1 = gcurve(color=color.blue)
    theta = 0*pi/180
    dtheta = 1*pi/180

    while theta < 89*pi/180:
        trange = get_range(theta, v0, initial_position, mass, radius)
        f1.plot(theta*180/pi, trange)
        theta += dtheta

def get_best_angle(v0, initial_position, mass, radius):
    theta = 0*pi/180
    dtheta = 1*pi/180

    maxrange = 0
    maxangle = 0

    while theta < 89*pi/180:
        trange = get_range(theta, v0, initial_position, mass, radius)
        if trange > maxrange:
            maxrange = trange
            maxangle = theta
        theta += dtheta
    print(str(maxrange) + ' at ' + str(maxangle*180/pi))
    return maxangle

def plot_angle_by_velocity(max_velocity, initial_position = vector(0,0,0),
                           mass = 0.05, radius = 0.2):
    g1 = graph(xtitle = "velocity", ytitle = "best angle")
    f1 = gcurve(color = color.blue)
    velocity = 0
    dv = 5
    while velocity <= max_velocity:
        best_angle = get_best_angle(velocity, initial_position, mass, radius)
        f1.plot(velocity, best_angle*180/pi)
        velocity += dv

get_best_angle(10, vector(0,0,0), 5, 2)
time.sleep(10)