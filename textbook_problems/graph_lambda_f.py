import matplotlib.pyplot as plt
import numpy as np
"""From Physics for Scientists and Engineers chapter 1, problem 52:
plot  frequency on the vertical axis and 1/lambda on the horizontal axis"""


figure, ax = plt.subplots()

ax.set_ylabel('frequency [1/s]')
ax.set_xlabel('1/lambda')

frequencies = [440, 493.9, 523.2, 587.3, 659.3, 698.5, 784]
wavelength = [0.78, 0.6949, 0.6559, 0.5843, 0.5206, 0.4914, 0.4378]

one_over_lambda = []
for i in wavelength:
    one_over_i = 1/i
    one_over_lambda.append(one_over_i)

slope, intercept = np.polyfit(one_over_lambda, frequencies, 1)
slope = round(slope, 4)
ax.annotate('slope = ' + str(slope), xy=(0.05, 0.90),
            xycoords='axes fraction')
plt.plot(one_over_lambda, frequencies)
plt.show()