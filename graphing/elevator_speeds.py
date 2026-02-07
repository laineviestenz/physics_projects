import matplotlib.pyplot as plt

positions = []
times = []

print("Enter positions and times, enter 'x' when finished")

while True:
    position = input("Enter Position: ")
    if position == 'x':
        break
    try:
        float(position)
    except ValueError:
        print('Please enter a valid input.')
        position = input("Enter Position: ")
    else:
        positions.append(position)
    
    time = input('Enter Time: ')
    if time == 'x':
        break
    try:
        float(time)
    except ValueError:
        print('Please enter a valid input.')
        position = input("Enter Time: ")
    else:
        times.append(time)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(positions, times)
plt.show()