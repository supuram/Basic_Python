import math
import numpy as np
print(math.exp(2))

vector = np.vectorize(np.exp)
r = np.linspace(0, 20)
a = 0.59
p = vector(r)
s3 = r * p
