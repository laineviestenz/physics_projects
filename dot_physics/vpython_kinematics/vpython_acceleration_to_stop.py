#initial position/time
x = 0
t = 0
#initial velocity
v = 0.45
#acceleration
a = -0.2
#calculation increment
dt = 0.01

while v > 0:
    #increase the velocity by aceleration * time interval
    v += a * dt
    #use the new velocity and the previous x position to calculate new position
    x += v * dt
    #increase time by increment
    t += dt
print(v)
print('x =' + str(x))
print('t = ' + str(t))