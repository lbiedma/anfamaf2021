import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

datos = np.loadtxt("../../datos/datos_aeroCBA.dat")
# para windows
# datos = np.loadtxt("C:\\Documentos\\datos\\datos_aeroCBA.dat")

anios = datos[:,0]
temps = datos[:,1]

not_nan = ~np.isnan(temps)

anios_interp = anios[not_nan]
temps_interp = temps[not_nan]

polinomio = interp1d(anios_interp, temps_interp, kind='cubic', fill_value='extrapolate')

anios_plot = np.arange(1957,2018)
temps_plot = polinomio(anios_plot)
#[polinomio(anio) for anio in anios_plot]

plt.plot(anios_plot, temps_plot)
plt.plot(anios_interp, temps_interp,'o')
plt.grid()
plt.show()
