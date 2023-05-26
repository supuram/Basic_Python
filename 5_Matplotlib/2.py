#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

r = np.linspace(0, 20)
a=0.59
s3 = r * r * math.exp(-2*r/(3*a)) * (1-((2*r)/(3*a))+((2*r*r)/(27*a*a)))**2
p3 =  r * r * math.exp(-2*r/(3*a)) * ((r/a)-((r*r)/(6*a*a)))**2
d3 = r * r * (r * r * math.exp(-r/(3*a))) ** 2


plt.plot(r,s3,label = '3s')
plt.plot(r,p3,label = '3p')
plt.plot(r,d3,label = '3d')
plt.xlabel('r')
plt.ylabel('r2R2')
plt.legend()
plt.show()
# %%
