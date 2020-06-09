import torch
from torch import nn,optim
import matplotlib.pyplot as plt
import numpy as np
# #模型框架搭建 生成数据
# x = torch.unsqueeze(torch.arange(-10,10),dim=1).reshape(20,1)
# y = x.pow(3)
#
# class net(nn.Module):
#     def __init__(self):
#         super().__init__()
#         #定义神经元
#         self.w1 = nn.Parameter(torch.randn(1,4))
#         self.b1 = nn.Parameter(torch.zeros(4))
#         self.w2 = nn.Parameter(torch.randn(4, 4))
#         self.b2 = nn.Parameter(torch.zeros(4))
#         self.w3 = nn.Parameter(torch.randn(4, 1))
#         self.b3 = nn.Parameter(torch.zeros(1))
#     def forward(self,x):
#         lc1 = torch.sigmoid(torch.matmul(x,self.w1)+self.b1)
#         lc2 = torch.sigmoid(torch.matmul(lc1, self.w2) + self.b2)
#         lc3 = (torch.matmul(lc2, self.w3) + self.b3)
#         return lc3
#
# if __name__ == '__main__':
#     md1 = net()
#     opt = optim.Adam(md1.parameters(),lr=0.001)
#     lossfunc = nn.MSELoss()
#     plt.ion()
#     for i in range(10000):
#         out = md1(x.float())
#         loss = lossfunc(out,y.float())
#
#         opt.zero_grad()
#         loss.backward()
#         opt.step()
#
#         if i %5==0:
#             plt.cla()
#             plt.plot(x,y,c='r')
#             plt.plot(x,out.detach().numpy(),c='g')
#             plt.pause(0.01)
#             print(loss.item())
#     plt.ioff()
#     plt.show()

#生成布尔矩阵，布尔索引
# data = torch.arange(-10,10).reshape(5,4)
# c = torch.tensor([False,True,False,True,False])#注意形状
# print(c)
# a = data[data>2]
# c = data[c]
# print(c)
# print(a)
# print(data[0])
# print(data[(1,2),])
# print(data[(1,2)])

# x = np.array([[0,1,2],
#               [3,4,5],
#               [6,7,8],
#               [9,10,11]])
# print(x[[[0],[3]],[0,2]])
# x = np.arange(0,16).reshape(8,2)
#位置形状+位置索引
x = np.arange(10*20*30).reshape(10,20,30)
ind = np.zeros(shape=(1,2,1),dtype=np.int64)
ind2 = np.zeros(shape=(3),dtype=np.int64)

result = x[...,ind,:]
# y = np.arange(30)
# print(x[...,ind,:].shape)
# print(result[...,1,2,3,:].shape)
# print(x[...,ind,:])
# print(x[...,ind,[[0,1],[0,1]]])
# print(x[...,[0]].shape)
# print(x[...,[0,1,2],[0],[0]])#省略号取剩下的维度，冒号取1个维度
# x = np.arange(2*3*4).reshape(2,3,4)

# print(x*y)


x = np.arange(1*2*3*4*5).reshape(5,4,3,2,1)
ind = np.zeros(shape=(1,2,3),dtype=np.int64)
ind2 = np.zeros(shape=(2,3),dtype=np.int64)
y1 = x[...,ind,:,ind2]
y2 = x[...,ind,ind2,:]
print(x[:,:,])
print(y1.shape)
print(y2.shape)
# print(x)
print('=====y1=======\n',y1)
# print(y2[0])



# print(x)print(x[ind,:,ind2].shape)
# print(x[ind,:,ind2])
# print(x)