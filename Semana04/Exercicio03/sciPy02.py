## Interpolação

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.linspace(0, 10, 10)
y = x**2 * np.sin(x)
plot.scatter(x,y)
# Retorna o gráfico com os 10 pontos

from scipy.interpolate import interpid

f = interpid(x ,y,  kind='linear')

x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)

plt.plot(x_dense, y_dense)
# Retorna uma interpolação linear 

#----------------------------------

# Para uma interpolação cúbica, nós teríamos

f = interpid(x ,y,  kind='cubic')

x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)

plt.plot(x_dense, y_dense)



