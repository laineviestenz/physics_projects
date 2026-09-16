import numpy as np
import matplotlib.pyplot as plt

wavelength = np.array([656.3,486.1,434.1,410.2,397.0,388.9,383.5])
n = np.arange(3,10,1)

R = 1/(wavelength*(0.25-(1/n**2)))

print(R)
x = ((1/4)-(1/(n**2)))
y = (1/wavelength)

fit_x = x.copy()
#extend fit functions to x=0 and 0.3 past the last data point
fit_x[0] = 0
fit_x[-1] = x.max()+0.03

m, b = np.polyfit(x, y, 1)

plt.style.use("seaborn-v0_8")
plt.scatter(x, y)
plt.plot(fit_x, m*fit_x+b)
plt.title("Hydrogen Spectrum Rydberg Constant", size=20, fontweight="bold")
plt.ylabel(r"$\frac{1}{\lambda}$" + "(nm)", size=15)
plt.xlabel(r"$\frac{1}{4} - \frac{1}{n^2}$")
plt.text(0.01, 0.0025, "R = " + str(round(m,2)), size=15, bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="black"))
plt.xlim(0, right = None)
plt.ylim(0, top = None)
plt.show()