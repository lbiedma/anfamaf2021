from ej2 import *
import matplotlib.pyplot as plt

x = [-1,0,1]
y = [0,-1,0]

h = 4/199
z = [-2 + i*h for i in range(200)]

w = inewton(x,y,z)

plt.plot(z,w)
plt.plot(x,y,'x')
plt.show()
