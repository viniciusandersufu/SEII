import numpy as np

l = [1,2,3] # lísta
a = np.array([1,2,3]) # array

# se nós quisermos adicionar um elemento a uma lista, podemos fazê-lo de duas maneiras:

l.append(4) #resultado l = [1,2,3,4]
# ou
l = l + [4] #resultado l = [1,2,3,4]

# não existe atributo 'append' para arrays, mas se tentarmos de forma análoga à segunda opção:

a = a + np.array([4]) # o array continua tendo 3 elementos, mas cada elemento sofreu uma adição de 4 unidades. 

l = l * 2 # resultado l = [1,2,3,1,2,3]
a = a * 2 # resultado a = [2,4,6]

