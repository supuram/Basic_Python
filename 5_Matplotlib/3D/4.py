from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Spherical Coordinate

theta = np.linspace(-np.pi, np.pi)
phi = np.linspace(-np.pi/2, np.pi/2)
THETA, PHI = np.meshgrid(theta,phi)

R = np.cos(phi) 
X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(PHI)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()