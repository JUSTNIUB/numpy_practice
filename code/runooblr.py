import numpy as np

a = np.arange(24)
print(a.ndim)
b = a.reshape(2,4,3)
print(b.ndim)

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
a.shape = (3,2)#shape也可以用来调整数组大小
print(a)

#创建数组
x = np.empty([3,2],dtype=int)
print(x)
x = np.zeros((5,5))

print(x)
print(np.ones((5,5)))
print(np.eye(5))

#从数值范围创建数组
x = np.arange(5)
print(x)
x = np.arange(5,dtype=float)
print(x)
x = np.arange(10,20,2)
print(x)

#切片和索引
a = np.arange(10)
s = slice(2,7,2)
print(a[s])
print(a[2:7:2])
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[...,1])
print(a[1,...])
print(a[...,1:])
#高级索引
x = np.array([[1,2],[3,4],[5,6]])
y = x[[0,1,2],[0,1,0]]
print(y)
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x)
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print(y)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a[1:3,1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)

#布尔索引
print(a>5)
print(a[a>5])
#广播
#满足以下其中之一即可广播
#形状相同
#维度相等，各个维度上的长度相等或者为1，如果有一个维度不相等则不可广播
#输入数组在维度为1的方向上，广播时沿着此维度运算时都沿用第一组的值
a = np.arange(12).reshape(4,3)
b = np.arange(3).reshape(1,3)
print(a.shape,b.shape)
print(a*b)



