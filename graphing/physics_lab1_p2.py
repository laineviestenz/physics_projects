import numpy as np
import matplotlib.pyplot as plt

wavelength = np.array([656.3,486.1,434.1,410.2,397.0,388.9,383.5])
n = np.arange(3,10,1)

R = 1/(wavelength*(0.25-(1/n**2)))

print(R)
#x=n, y = 1/(R(0.25-(1/n**2)))
plt.scatter(n, wavelength)
plt.ylabel(r"$\frac{1}{\lambda}$" + "(nm)", size=15)
plt.xlabel(r"$\frac{1}{4} - \frac{1}{n^2}$")
plt.show()