import numpy as np

print("zeros/ones/empty")
x = np.zeros((2,3),dtype=np.int8)
print(x)
print(x.dtype)
x = np.empty((2,3))
print(x)
x =np.ones((2,3))
print(x)

print("使用arange 生成连续的元素")
print(np.arange(6))
print(np.arange(1,8))
print(np.arange(1,8,0.2))
a = np.arange(20)
print(a)
a = a.reshape(4,5)
print(a)

print("使用astype复制数组，并改变类型")
x = np.array([1,2,3,4,5],dtype=np.float32)
y = x.astype(np.int8)
print(x)
print(y)

print('将字符串类型的元素转为数值元素')
x = np.array(['1','2','3','4','5'])
y = x.astype(np.int8)
z = y.astype(np.str)
print(x,y,z)

print('使用其他数组的元素的数据类型作为参考')
x = np.array([1,2,3,4],dtype=np.float64)
y = np.array([1,2,3],dtype=np.int8)
print(y)
print(y.astype(x.dtype))


print('ndarray的运算 也有用到广播的思想在这里？？ 相关所有运算符操作都是经过了重载,要保证两侧形状在广播后一致')
x = np.array([1,2,3])
print(x*2)
y = x<2
print(y)
print(type(y),y.dtype)

y = np.array([3,4,5])
print(x*y)
z = x>y
print(z)


print('=================================')
print('ndarray的轴')
print('=================================')
x = np.arange(8).reshape((2,4))
print(x)
print("维度",x.ndim)
print(x.T)
print(np.dot(x,x.T))#dot的使用需要注意，在ab都是二维时，进行的是矩阵乘法。如果是一维，则是内积

#高维转置难以想象
x = np.arange(27).reshape((3,3,3))
print(x)
print(x.T)

k = np.arange(24).reshape(2,3,4)
print(k)
print(k[0][1][0])
#轴变换
k = k.transpose(1,0,2)
print(k.shape)
#轴交换
k = k.swapaxes(0,2)
print(k.shape)
print(k.T.shape)
#轴交换做转置
k = np.arange(8).reshape(2,4)
# print(k)
# print(k.swapaxes(1,0))




print('=================================')
print('numpy的基本统计')
print('=================================')
#到底咋算的？？？？？ 迷 针对的作用域不同？ 最外层的取全部的，然后每个元素都算到？
x = np.array([[[1,2],[1,2]],[[3,4],[3,4]],[[5,6],[5,6]]])

print("形状",x.shape)
print("数据",x)
print("所有元素平均数",x.mean())
print("1维",x.mean(axis=1))
print("0维",x.mean(axis=0))
print('2维',x.mean(axis=2))
print("所有元素加和",x.sum())
print("0维数据加和",x.sum(axis=0))
print("1维数据加和",x.sum(axis=1))
print("2维数据加和",x.sum(axis=2))
print("统计最大数据",x.max())
print("统计最大数据0维",x.max(axis=0))
print("统计最大数据1维",x.max(axis=1))
print("统计最大数据2维",x.max(axis=2))

print('=================================')
print('numpy的where函数')
print('=================================')
x = np.array([1,2,3,4,5,6])
x = np.where(x>2,4,5)
print(x)

print('=================================')
print('ndarray的存取')
print('=================================')
x = np.array([[1,2,4],[3,4,5],[6,4,2]])
np.save("file",x)
y = np.load("file.npy")
print(y)

print('=================================')
print('矩阵求逆')
print('=================================')
x = np.array([[1,1],[1,2]])
y = np.linalg.inv(x)
print(y)
print(x.dot(y))
print(x@y)
print(np.matmul(x,y))

print('=================================')
print('numpy 随机数')
print('=================================')
x = np.random.randint(0,2,10000)#离散均匀分布
x = np.random.randn(20)
print(x)
print((x>0).sum())