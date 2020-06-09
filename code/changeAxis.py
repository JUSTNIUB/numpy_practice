#维度变换，在计算机中是如何做的
import numpy

print('维度变换，axis的变换方式')

orgData = numpy.arange(0,12)
orgData = orgData.reshape(3,2,2)
print("原始数据形状",orgData.shape)
print("原始数据\n",orgData)
mdfData = orgData.transpose(2,1,0)
print('0 2轴交换数据\n',mdfData)
mdfData = orgData.transpose(1,0,2)
print('1,0,2 交换数据',mdfData)
mdfData = orgData.swapaxes(1,2)
print('交换12轴数据',mdfData)
#自定义python 多维转换 a[i][j][k] = b[j][k][i] 取出不同元素
# sizeArray = orgData.shape
# rankargs  = [2,1,0]
# newSizeArray = [sizeArray[rank] for rank in rankargs]
# print(len(newSizeArray))
# arrayindex = [0,0,0]
# print(arrayindex)
