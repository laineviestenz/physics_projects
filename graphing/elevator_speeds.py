import matplotlib.pyplot as plt

positions = []
times = []

print("Enter positions and times, enter 'x' when finished")

while True:
    position = input("Enter Position: ")
    if position == 'x':
        break
    time = input('Enter Time: ')
    if time == 'x':
        break
    positions.append(position)
    times.append(time)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(positions, times)
plt.show()