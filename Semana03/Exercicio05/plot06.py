import matplotlib.pyplot as plt
import numpy as np

x1 = np.arrange(0,1000,1) # cria um array entre 0  e 1 000 com saltos de 1 unidade
#print(x1)

plt.plot(x1,x1**2) # cria uma função y = x1² em função de x1
plt.show()


