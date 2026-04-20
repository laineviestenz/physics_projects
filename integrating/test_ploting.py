import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = [i for i in range(0, 50)]
y = []

for a in x:
    y.append(a**2)

plt.plot(x, y)
plt.show()