from vpython import *
import time

f1 = gcurve()
#the particle is at position 0 when t = 0
x = 0
t = 0
#set the velocity
v = 0.45
a = 0.8
#set the increment that will be used to calculate position
dt = 0.25

while t < 2.5:
    #increase the velocity by aceleration * time interval
    v += a * dt
    #use the new velocity and the previous x position to calculate new position
    x += v * dt
    #increase time by increment
    t += dt

    f1.plot(t,x)
time.sleep(10)