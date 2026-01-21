from vpython import *

A = vector(1, 3, -1)
print(A)

B = vector(0, 1, -4)
print(B)

C = A+B
print(C)

#This gives the x component of the vector
print(C.x)

#gives the magnitude of C
print(mag(C))

#2 different ways to print the unit vector version
print(hat(C))
print(norm(C))

#print dot and cross products
print(dot(A, B))
print(cross(A, B))