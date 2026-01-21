from vpython import *
import time

g1 = graph(title = 'Velocity vs. Time', xtitle = 'Time (s)', ytitle = 'Velocity (m/s)', width = 1500, height = 750, fast = False)
f1 = gcurve()

x = 0
t = 0
v = 15
a = -9.8
dt = 0.01

while t < 5:
    t += dt
    v += a * dt
    x += v * dt
    f1.plot(t, x)
time.sleep(15)