import matplotlib.pyplot as plt
from input_functions import get_valid_position as get_valid_position
from input_functions import get_valid_time as get_valid_time
positions = []
times = []

print("Enter positions and times, enter 'x' when finished")

while True:
    pos = get_valid_position()
    #the function returns none if x is typed, so the loop breaks if it returns None
    if pos == None:
        break
    else:
        positions.append(pos)
    
    times.append(get_valid_time(times))
    
plt.style.use('classic')
fig, ax = plt.subplots()
ax.set_xlabel('time [seconds]')
ax.set_ylabel('position [stories]')
ax.plot(times, positions)
ax.set_ybound(lower = 0, upper=max(positions)*1.1)
plt.show()