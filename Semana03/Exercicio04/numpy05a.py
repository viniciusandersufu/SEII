# produto escalar

l1 = l = [1,2,3] # lísta1
l2 = [4,5,6] # lísta2
a1 = np.array([1,2,3]) # array1
a2 = np.array(l2) # array2

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1,a2)
print(dot)


