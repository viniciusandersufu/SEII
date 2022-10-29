## Otimização

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.optimize import minimize

def f(x):
    return (x-3)**2

res = minimize(f, 2)

res.x[0]
# Retorna 2.99999...


#----------------------------------

f = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2

cons = ({'type': 'ineq', 'fun': lamba x: x[0]-2*x[1]+2},
        {'type': 'ineq', 'fun': lamba x:-x[0]-2*x[1]+6},
        {'type': 'ineq', 'fun': lamba x:-x[0]+2*x[1]+2})
bnds = ({0, None}, {0, None})
res = minimize(f, (2,0), bounds = bnds, constrainsts=cont)

res.x
