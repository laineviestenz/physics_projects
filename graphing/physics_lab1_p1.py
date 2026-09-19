import matplotlib.pyplot as plt
import numpy as np


x = np.array([1.44, 0.93, 0.70, 0.54, 0.46, 0.40, 0.34, 0.30, 0.27, 0.24])
y = np.array([2.3, 2.57, 2.7,2.79,2.85,2.88,2.92,2.94,2.96,2.98])

fig, ax = plt.subplots()
plt.style.use('seaborn-v0_8')
plt.scatter(x,y)

m,b = np.polyfit(x,y,1)
a = np.arange(0,max(x)+0.5, 0.1)

plt.plot(a, m*a+b)
plt.grid(True, "both")
plt.xlabel("Current (I) in Amps")
plt.ylabel("Voltage (V) in Volts")
plt.title("Internal Resistance and emf of Battery\nVoltage as a Fnction of Current and Applied Resistance")
plt.xlim(0, right=None)
plt.ylim(0, top=None)
t = plt.text(0.1,2.1, "emf = " + str(round(b, 2)) + "\nr = " + str(abs(round(1/m,2))),
              size=15, bbox=dict(boxstyle="square,pad=0.3", fc = "white", ec="black"))
plt.show()