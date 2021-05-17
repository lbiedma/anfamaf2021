import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos3a.dat')

# y = C * x ** A --> ln(y) = ln(C * x ** A)
#                    ln(y) = ln(C) + A * ln(x)
#y_p =ln(y)
#x_p = ln(x)
#B = ln(C)            y_p = B  + A * x_p 


x = datos[0]
y = datos[1]

x_p = np.log(x)
y_p = np.log(y)

coefs = np.polyfit(x_p, y_p, 1)

A = coefs[0]
C = np.exp(coefs[1])

print(f'Coef. A = {A}, Coef C = {C}.')

plt.plot(x,y, 'o')
plt.plot(x, C * x ** A)
plt.show()