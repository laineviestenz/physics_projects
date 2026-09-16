import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45,
                 50, 55, 60, 65, 70, 75, 80, 85, 90])

voltage = np.array([999, 830, 743, 656, 580, 513, 453, 401, 350, 310,
                    269, 243, 215, 190, 167, 150, 131, 114, 103])



plt.yscale('log')
plt.grid(True, which='both')
plt.plot(time, voltage)
plt.show()