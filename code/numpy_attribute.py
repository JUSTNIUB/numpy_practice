import torch
import numpy as np

a = np.array([1,2,3])
b = [1,2,3]
c = torch.tensor([1,2,3])
print(type(a))
print(a.dtype)
print(type(b))
print(type(c))
print(c.dtype)
data = [[1,2,3,4,5],[1,2,3,4,5]]
print('=================================')
print('numpy的属性')
print('=================================')
x = np.array(data)

print(x)
print(type(x))
print(x.dtype)
print(x.shape)
print(x.ndim)
print(x.size)
x = x.reshape(2,5,1)
print(x.ndim)