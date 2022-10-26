import numpy as np

a = np.array([1,2,3,4])

print(a)
print(a.shape) #[4,]
print(a.dtype) #int64 (elementos inteiros com 64 bits)
print(a.ndim) #1
print(a.size) #4 (número de elementos)
print(a.itemsize) #8 (número de bytes de cada elemento)
