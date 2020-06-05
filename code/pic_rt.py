import matplotlib.pyplot as plt
ax =[]
ay =[]
plt.ion()
for i in range(100):
    ax.append(i)
    ay.append(i**2)
    plt.clf()
    # plt.scatter(ax,ay,c='r',marker='D')
    plt.plot(ax,ay,c='r',marker='D')
    plt.pause(1)

plt.ioff()
plt.show()