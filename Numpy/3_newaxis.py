import numpy as np

a = np.linspace(1,20,10)
b = a[np.newaxis, :]
print(b.shape)

c = a[:, np.newaxis]
print(c.shape)