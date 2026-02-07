import matplotlib.pyplot as plt
from input_functions import check_nan as cknan
from input_functions import check_empty as ckempty
positions = []
times = []

print("Enter positions and times, enter 'x' when finished")

run = True
while run == True:
    while True:
        position = input("Enter Position: ")
        if position == 'x':
            run = False
            break
        if cknan(position) and ckempty(position) == True:
            positions.append(position)
            break
        else:
            print('please enter a valid number')
    if run == False:
        break
    
    while True:
        time = input("Enter Time: ")
        if cknan(time) and ckempty(time) == True:
            times.append(time)
            break
        else:
            print('please enter a valid number')

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(positions, times)
plt.show()