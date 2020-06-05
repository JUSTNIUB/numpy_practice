import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x = np.random.normal(0,1,100)
y = np.random.normal(0,1,100)
z = np.random.normal(0,1,100)#正态分布
z1 = np.random.normal(0,1,100)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z,c='green',marker='v',label='boy')
ax.scatter(x,y,z1,c='red',marker='8',label='girl')
ax.scatter(0,0,0,c='yellow',marker='D')
plt.legend()
plt.show()