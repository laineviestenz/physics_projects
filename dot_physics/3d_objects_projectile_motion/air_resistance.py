from vpython import *
import time
"""This is a model of two balls, one behind the other, with different masses,
being thrown with an initial velocity, and shows the effect of air resistance."""

# Force air = -1/2*rho*A*C*magnitude(p)^2/m^2*normalized(p)
# where rho = density, A = cross sectional area, C = Drag coefficient, v = velocity
#create the ground
ground = box(pos=vector(0,0,0), size=vector(8,0.2,4), emissive=True)

#create the balls
ball1 = sphere(pos=vector(-3.5,0.6,0.75), radius=0.5, color=color.yellow,
               make_trail = True, emissive=True)
ball1.mass = 0.05
ball2 = sphere(pos=vector(-3.5,0.6,-0.75), radius=0.5, color=color.cyan,
               make_trail=True, emissive=True)
ball2.mass = 0.05

#define physical constants and initial conditions
g = vector(0,-9.8,0)
v0 = 10
theta = 40*pi/180
t = 0
dt = 0.01
rho = 1.2
c = 0.47
ball1.area = pi * ball1.radius**2

#find initial momentum
ball1.momentum = v0*vector(cos(theta), sin(theta), 0) * ball1.mass
ball2.momentum = v0*vector(cos(theta), sin(theta), 0) * ball2.mass

#play animation
while ball2.pos.y >= ground.pos.y + ground.size.y/2 + ball1.radius:
    #set simulation rate
    rate(50)
    
    #force = mass * gravity
    ball1.airresistance = -0.5 * rho * ball1.area * c * mag(ball1.momentum)**2 * norm(ball1.momentum)/ball1.mass**2
    ball1.force = ball1.mass*g + ball1.airresistance
    ball2.force = ball2.mass*g
    
    #determine the velocity by adding the product of acceleration and dt
    #ball1.velocity += g*dt
    ball1.momentum += ball1.force * dt
    ball2.momentum += ball2.force * dt

    #determine the postition by adding the change in position to the last pos
    ball1.pos += ball1.momentum * dt / ball1.mass
    ball2.pos += ball2.momentum * dt / ball2.mass

    t = t + dt

time.sleep(10)