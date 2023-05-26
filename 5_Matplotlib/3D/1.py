from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
x = np.linspace(0, 10, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x,y)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X, Y, Z)
ax.set_zlim(0,2)

ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()