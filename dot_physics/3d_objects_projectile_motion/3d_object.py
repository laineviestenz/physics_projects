"""make a 3D model of ball going up and falling from the air"""
from vpython import *
import time

ball = sphere(pos = vector(-2,0.2,0), radius = 0.05, color = color.yellow, make_trail = True)
ground = box(pos = vector(0,0,0), size = vector(4.5,0.02,0.25))

g = vector(0,-9.8,0)
mball = 0.05
v0 = 7.4
theta = 73*pi/180
ball.p = v0*vector(cos(theta), sin(theta), 0)*mball
vscale = 0.1
#varrow = arrow(pos = ball.pos, axis = vscale*vball, color = color.cyan)

ball2 = sphere(pos = vector(-2,0.2,0), radius=ball.radius, color=color.cyan, make_trail = True)
ball2.m = 0.005
ball2.p = v0*vector(cos(theta), sin(theta), 0)*ball2.m
t = 0
dt = 0.01

print (ball.pos.y)
while ball.pos.y > ground.pos.y + ground.size.y/2 + ball.radius:
    rate(100)
    f = mball*g
    a = f/mball
    vball = vball + a*dt
    ball.pos = ball.pos + ball.p * dt/ball.m
    f2 = ball2.m*g
    #varrow.pos = ball.pos
    #varrow.axis = vscale*vball
    t = t + dt
print (ball.pos.y)
print (ground.pos.y + ground.size.y/2 + ball.radius)
time.sleep(10)