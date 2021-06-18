import matplotlib.pyplot as plt
import numpy as np

# restricciones
# 50*x + 24*y <= 2400 (1)
# 30*x + 33*y <= 2100 (2)

x = np.linspace(0,50,100)

y1 = (2400 - 50*x)/24
y2 = (2100 - 30*x)/33

restricciones = np.minimum(y1,y2)

restricciones = np.maximum(restricciones,0)

# plt.plot(x,y1)
# plt.plot(x,y2)

# plt.fill_between(x,y1,alpha=0.5)
# plt.fill_between(x,y2,alpha=0.5)

## CURVAS DE NIVEL ##

levels = np.linspace(40,80,5)

for level in levels:
	# x+y = level
	y = level - x
	plt.plot(x,y,label=f"nivel={level}")

plt.fill_between(x,restricciones,alpha=0.3)

plt.grid()
plt.legend()

plt.show()
