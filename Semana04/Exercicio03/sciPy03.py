## Ajuste de curvas

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2

plt_scatter(x_data, y_data)
# Retorna a figura com os 10 pontos

# Ajuste desses dados a uma função quadrática y = ax² + b

from scipy.optimize import curve_fit

def func(z, a, b):
    return a*x**2 + b

popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1))

popt
# Retorna 'array([3., 2.])

