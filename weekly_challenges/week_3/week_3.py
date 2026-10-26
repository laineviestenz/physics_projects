import numpy as np

def simulate_velocity(dt, n_steps):
    """return NumPy arrays of times and velocities"""
    v = 0
    t = 0
    y = 0
    dv = 9.8 #m*s^-2
    count = 0
    velocities = np.array([])
    times = np.array([])
    positions = np.array([])
    while count <= n_steps:
        velocities = np.append(velocities, v)
        times = np.append(times, t)
        positions = np.append(positions, y)
        v += dv*dt
        t += dt
        y = y + (v*dt)
        count += 1
    return velocities, times, positions

v1, t1, y1 = simulate_velocity(0.1,20)
v2, t2, y2 = simulate_velocity(0.05,40)
real = 1/2 * 9.8 * 2**2

print(f"dt = 0.1: y(2) = {y1[-1]}\ndt = 0.05: y(2) = {y2[-1]}")
print(f"Errors:\n dt=0.1: {np.abs(real-y2[-1])}\ndt=0.05:{np.abs(real-y1[-1])}")