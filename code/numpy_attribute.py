import torch
import numpy as np


#创建数据对象
tmpdata = [1,2,3,4,5,6,7,89,10]
npdata = np.arange(0,1,0.1)
print('arange 创建矩阵',npdata)
npdata = np.array(tmpdata)
print('从别的类型重载数据',npdata)
npdata = np.random.randn(10)
print('标准正态分布randn ',npdata)
npdata = np.random.rand(10)
print('均匀分布rand ',npdata)
npdata = np.random.randint(0,10,5)
print('整数 均匀分布',npdata)
#矩阵生成
print("单位矩阵",np.eye(3))
print("下三角矩阵\n",np.tril(np.ones((3,3))))#输入为矩阵
print("0矩阵\n",np.zeros((4,5)))
#输入的是一维数组就输出二维数组,输入二维数组就输出一维数组
print('对角矩阵\n',np.diag(np.random.randint(1,10,9)))

#和torch相互转换
print("转成torch",torch.from_numpy(np.random.randint(10,20,10)))
print("转成numpy",torch.randint(5,(10,1)).numpy())

#查看属性
print('========================')
npdata = np.arange(0,20).reshape(4,5)
print(npdata)
print("dtype:",npdata.dtype)
print('ndim',npdata.ndim)
npdata = npdata.reshape(5,2,2)
print('size',npdata.size)
print('shape',npdata.shape)
npdata = npdata.transpose(1,0,2)
print("shape after transpose",npdata.shape)
npdata = npdata.swapaxes(0,1)
print("shape after swapaxes",npdata.shape)
print("astype new matrix:\n",npdata.astype(np.str))
npdata = npdata.T.reshape(2,2,5)
print("转置",npdata)
print(npdata.shape)
#这里从内存角度去理解可能会好一点。axis表示的是从第几个维度去进行统计的。那么它是怎么找到要求的平均数在哪个位置呢？
#假设矩阵是mxn，那么它的大小可以表示为mxn个字节，第一行从0位置开始，第二行从n位置开始....第m行从(m-1)*n位置开始
#当axis =0时，它计算第一个平均值时会取0，n，....(m-1)*n来计算，计算第二个时会取1,n+1,...(m-1)*n+1，直到计算完所有的平均值.
#当axis=1时，寻址的位移发生改变了。这时其中一个元素的大小变成了一个字节，取平均值则是按照
print('求平均数',npdata.mean())
print('求行平均数',npdata.mean(axis = 0))
print('求列平均数',npdata.mean(axis = 1))
print('求2维平均数',npdata.mean(axis=2))

