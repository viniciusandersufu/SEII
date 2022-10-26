import numpy as np

a = np.array([1,2])
print(a.shape) #array de 1 dimensão (2 colunas e 1 linha)

b = np.array([1,2], [3,4], [5,6])
print(b.shape) # array de 2 dimensões (2 colunas e 3 linhas)
print(a[0]) # mostra a primeira linha do array
print(a[0,:]) # printa toda a primeira linha do array
print(a.T) # Transpõe o array

