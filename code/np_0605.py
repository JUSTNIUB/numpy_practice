import torch
from torch import nn
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.arange(-10,10),dim=1)
y = x.pow(3)

# plt.scatter(x,y)
# plt.show()
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(1,20))
        self.b1 = nn.Parameter(torch.zeros(20))
        self.w2 = nn.Parameter(torch.randn(20, 64))
        self.b2 = nn.Parameter(torch.zeros(64))
        self.w3 = nn.Parameter(torch.randn(64, 256))
        self.b3 = nn.Parameter(torch.zeros(256))
        self.w4 = nn.Parameter(torch.randn(256, 64))
        self.b4 = nn.Parameter(torch.zeros(64))
        self.w5 = nn.Parameter(torch.randn(64, 1))
        self.b5 = nn.Parameter(torch.zeros(1))
    def forward(self,x):
        lc1 = nn.functional.sigmoid(torch.matmul(x,self.w1)+self.b1)
        lc2 = nn.functional.relu(torch.matmul(lc1,self.w2)+self.b2)
        lc3 = nn.functional.relu(torch.matmul(lc2,self.w3)+self.b3)
        lc4 = nn.functional.relu(torch.matmul(lc3,self.w4)+self.b4)
        lc5 = torch.matmul(lc4,self.w5)+self.b5
        return lc5

if __name__ == '__main__':
    net = Net()
    optim = torch.optim.Adam(net.parameters(),lr=0.01)
    loss_func = nn.MSELoss()
    plt.ion()
    for i in range(10000):
        out = net(x.float())
        loss = loss_func(out,y.float())

        optim.zero_grad()
        loss.backward()
        optim.step()

        if i%5==0:
            plt.cla()
            plt.scatter(x,y)
            plt.plot(x,out.detach().numpy(),'r')
            plt.pause(0.01)
            print(loss.item())
    plt.ioff()
    plt.show()