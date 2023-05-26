#%%
import matplotlib.pyplot as plt
import numpy as np

x1=x2 = np.linspace(0, 20, 100)
plt.plot(x1, np.sin(x1),label = 'sin x')
plt.plot(x2,np.cos(x2),label = 'cos x')
plt.xlabel('x')
plt.ylabel('sin x')
plt.legend()
plt.show()
# %%
