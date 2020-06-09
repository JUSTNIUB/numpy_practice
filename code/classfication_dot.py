import numpy as np
import torch
from torch import nn

import matplotlib.pyplot as plt
from math import pi
grad = np.arange(0,2*pi,pi/360)
step = np.arange(0,20,20/720)
grad1 = np.arange(pi,3*pi,pi/360)

a = np.array([step*np.cos(grad),step*np.sin(grad),np.zeros(step.shape)])
b = np.array([step*np.cos(grad1),step*np.sin(grad1),np.ones(step.shape)])

point = np.array([a.T,b.T])
point = point.reshape(1440,3)
np.random.shuffle(point)
x1 = torch.from_numpy(point[:,(0,1)])

flag = torch.from_numpy(point[:,2])
flag = flag.reshape(1440,1)
# print(x1,flag)

showdot = []
for i in range(-200,200,1):
    for j in range(-150,150,1):
        showdot.append([i,j,0])

showdot = np.array(showdot)/10
showdot = torch.from_numpy(showdot)

# xt1 = showdot[:,:1]
# xt2 = showdot[:,1:2]


# print(x.shape)
# plt.scatter(x,y,s=10,c='#007010',alpha=0.2)
# plt.show()

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(2,8))
        self.b1 = nn.Parameter(torch.zeros(8))
        self.w2 = nn.Parameter(torch.randn(8, 8))
        self.b2 = nn.Parameter(torch.zeros(8))
        self.w3 = nn.Parameter(torch.randn(8, 8))
        self.b3 = nn.Parameter(torch.zeros(8))
        self.w4 = nn.Parameter(torch.randn(8, 8))
        self.b4 = nn.Parameter(torch.zeros(8))
        self.w5 = nn.Parameter(torch.randn(8, 1))
        self.b5 = nn.Parameter(torch.zeros(1))
    def forward(self,x):
        lc1 = nn.functional.relu(torch.matmul(x,self.w1)+self.b1)
        lc2 = nn.functional.relu(torch.matmul(lc1,self.w2)+self.b2)
        lc3 = nn.functional.relu(torch.matmul(lc2,self.w3)+self.b3)
        lc4 = nn.functional.relu(torch.matmul(lc3,self.w4)+self.b4)
        lc5 = torch.sigmoid(torch.matmul(lc4,self.w5)+self.b5)
        return lc5
if __name__ == '__main__':
    net = Net()
    optim = torch.optim.Adam(net.parameters(),lr=0.01)
    loss_func = nn.MSELoss()
    plt.ion()
    for i in range(50000):
        out = net(x1.float())
        loss = loss_func(out,flag.float())

        optim.zero_grad()
        loss.backward()
        optim.step()

        if i%5==0:
            plt.cla()


            #画矩形
            xt1 = showdot[:,:2]
            # # print(xt1.shape)
            xt2 = net(xt1.float())#.detach().numpy()
            zerodot = xt1[xt2.reshape(xt2.numel())>0.5]
            onedot  = xt1[xt2.reshape(xt2.numel())<=0.5]
            # print(zerodot.shape)
            # print(zerodot.shape)
            # print(onedot.shape)

            #
            plt.scatter(zerodot[:,:1], zerodot[:,1:2], s=5, alpha=0.3,c ='#003070', label='zero')
            #plt.scatter(onedot[:,:1], onedot[:,1:2], s=1, c='#701000', alpha=1,label='one')

            a = x1[flag.reshape(flag.numel())==torch.tensor(1)]
            b = x1[flag.reshape(flag.numel())==torch.tensor(0)]

            plt.scatter(a[:,0], a[:,1], s=10, c='#007010', alpha=0.5)
            plt.scatter(b[:,0], b[:,1], s=10, c='#701000', alpha=0.5)
            plt.grid(b=False)
            plt.legend()
            plt.pause(0.01)
            print(loss.item())
    plt.ioff()
    plt.show()