"""for finding the positions, we will use the formula
Xn+1 = X + V*dt 
where we can find the updated position based on adding 'vt' to the previous
position"""

#the particle is at position 0 when t = 0
x = -0.5
t = 0
#set the velocity
v = 0.62
#set the increment that will be used to calculate position
dt = 0.1

while t < 2.2:
    """find the position of the particle, using a numerical model with 0.25
    second intervals"""
    #time incremented by 0.25 seconds(dt)
    t += dt
    #position increased by d = v*dt
    x += v*dt
print(t)    
print(x)