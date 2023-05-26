import numpy as np

a = np.linspace(1, 10, 20) # returns 100 (including 1 and 10) evenly spaced elements between 1 and 10
print(a)
print(a.size)
print(a.ndim)    # the dimension of the array
b = a.reshape(5, 4)   # reshapes a into 5 X 4 array
print(b)
c = a.reshape(5,2,2)
print(c)
print("Shape of c = ",c.shape)