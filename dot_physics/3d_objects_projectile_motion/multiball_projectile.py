from vpython import *
import time

#create the ground
ground = box(pos=vector(0,0,0), size=vector(8,0.2,4), emissive=True)

#create the balls
ball1 = sphere(pos=vector(-3.5,0.6,0.75), radius=0.5, color=color.yellow,
               make_trail = True, emissive=True)
ball1.mass = 0.05
ball2 = sphere(pos=vector(-3.5,0.6,-0.75), radius=0.5, color=color.cyan,
               make_trail=True, emissive=True)
ball2.mass = 500
#define physical constants and initial conditions
g = vector(0,-9.8,0)
v0 = 9
theta = 73*pi/180
t = 0
dt = 0.01

#find velocities
ball1.velocity = v0*vector(cos(theta), sin(theta), 0)
ball2.velocity = v0*vector(cos(theta), sin(theta), 0)

#play animation
while ball1.pos.y >= ground.pos.y + ground.size.y/2 + ball1.radius:
    #set simulation rate
    rate(50)
    
    #force = mass * gravity
    ball1.force = ball1.mass*g
    ball2.force = ball2.mass*g
    
    #acceleration = force/mass
    # ball1.acceleration = ball1.force/ball1.mass
    # ball2.acceleration = ball2.force/ball2.mass
    
    #determine the velocity by adding the product of acceleration and dt
    ball1.velocity += g*dt
    ball2.velocity += g*dt

    #determine the postition by adding the change in position to the last pos
    ball1.pos = ball1.pos + ball1.velocity*dt
    ball2.pos = ball2.pos + ball2.velocity*dt

    t = t + dt

time.sleep(10)