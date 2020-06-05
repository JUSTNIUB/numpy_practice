import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
x = np.random.randn(20)
y = np.random.randn(20)
z = np.random.randn(20)
x1 = np.random.randn(20)
y1 = np.random.randn(20)



#绘制点
plt.scatter(x,y,c='r',marker='p',s=20,label='girl')
plt.scatter(x1,y1,c='b',marker='p',s=18,label='boy')
plt.legend()#显示图例 即显示标签
plt.show()

#画气泡图
# sns.set(style='whitegrid')
# cm = plt.cm.get_cmap("RdYlBu")
# fig,ax = plt.subplots(figsize=(12,10))
#
# bubble = ax.scatter(x, y, s=(z - np.min(z) + 0.1) * 1000, c=z, cmap=cm, linewidth=0.5, alpha=0.5)
# ax.grid()
# fig.colorbar(bubble)
# ax.set_xlabel("pep",fontsize=15)
# ax.set_ylabel("pep som",fontsize=15)
# plt.show()