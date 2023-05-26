import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6, 9, 14])
y = np.array([0, 25, 50, 80])

plt.plot(x, y, marker = '*', ms = 15)
plt.show()