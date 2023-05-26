from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Spherical Coordinate

theta = np.linspace(0, 2*np.pi, 50)
phi = np.linspace(0, np.pi, 50)
THETA, PHI = np.meshgrid(theta,phi)

X = np.sin(THETA) * np.cos(PHI)
Y = np.sin(THETA) * np.sin(PHI)
Z = np.cos(PHI)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()