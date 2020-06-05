from PIL import Image,ImageFilter,ImageFont,ImageDraw
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
# img = Image.open(r"myimage/1.jpg")
# img.show()
# plt.imshow(img)
# plt.title('mt')
# plt.show(block=False)
# plt.pause(1)
# print(img.size)
# w,h=img.size
# print(w,h)
# bands = img.getbands()
# print(bands)
# mode = img.mode
# print(mode)
# img = img.resize((300,200))//创建了一个新的对象
# img.show()
# img.thumbnail((w//2,h//2),resample=Image.ANTIALIAS)#直接修改了原图
# img.show()
# img =img.crop((100,100,350,350))
# img.show()
# img =img.rotate(45)
# img.show()

# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img = img.filter(ImageFilter.BLUR)
# img.show()
# img = img.filter(ImageFilter.BoxBlur(radius=20))
# img.show()
# img = img.filter(ImageFilter.DETAIL)
# img.show()
# img = img.filter(ImageFilter.EMBOSS)
# img.show()
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()

# logo = Image.open("myimage/2.jpg")
# logo = logo.resize((50,50),resample=Image.ANTIALIAS)
# img.paste(logo,(100,100))
# img.show()

# #生成二维码
# class vrfcode():
#     def __init__(self):
#         return
#     def genChar(self):
#         return chr(random.randint(65,90))
#     def bgColor(self):
#         return (random.randint(0,120),
#                 random.randint(0,120),
#                 random.randint(0,120))
#     def frColor(self):
#         return (random.randint(150, 255),
#                 random.randint(150, 255),
#                 random.randint(150, 255))
#     def genPic(self):
#         w,h = 600,80
#         #生成画布
#         img = Image.new(mode='RGB',size=(w,h),color=(255,255,255))
#         #生成画笔
#         draw = ImageDraw.Draw(img)
#         #字体
#         font = ImageFont.truetype(font='Inkfree.ttf',size = 60)
#         #画背景
#         for i in range(w):
#             for j in range(h):
#                 draw.point(xy=(i,j),fill=self.bgColor())
#         #写字
#         for i in range(5):
#             draw.text(font=font,text=self.genChar(),fill=self.frColor(),\
#                       xy=(i*120+40,10))
#         img.show()
#         img.save('hello.jpg')
#
# testVcd = vrfcode()
# testVcd.genPic()

# x = np.random.normal(0,1,100)
# y = np.random.normal(0,1,100)
# z = np.random.normal(0,1,100)
#
# fig =plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x,y,z,c='b',marker='v')
# plt.show()

# ax = []
# ay = []
# plt.ion()
# for i in range(10):
#     ax.append(i)
#     ay.append(i**3)
#
#     plt.cla()  # 清除当前画板内容 cla会清除所有画板????
#     plt.plot(ax,ay)
#     plt.pause(0.1)
# plt.ioff()
# plt.show()

# x = np.random.normal(0,10,100)
# y = np.random.normal(0,10,100)
# z = np.random.normal(0,10,100)
# fig =plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x,y,z,s=100,c='b',marker='v',label='dddd')
# ax.legend()
# plt.show()

# imgpath = os.listdir("myimage")
# # print(imgpath)
# # plt.ion()
# for picname in imgpath:
#     img1 = Image.open(f"myimage/{picname}")
#     # plt.figure()
#     plt.imshow(img1)
#     plt.show(block=False)
#     plt.pause(1)
    # plt.cla()
# plt.ioff()
img = Image.open("myimage/1.jpg")
img.show()

# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()
# img = img.crop((100,100,700,700))
# img.show()
# img = img.rotate(90)
# img.show()
# r,g,b = img.split()
# img = Image.merge('RGB',(r.point(lambda i:i==i*0),
#                          g.point(lambda i:i==i*0),b))
# img.show()
# w,h =img.size
# img = img.resize((100,200))
# img.show()
#img.thumbnail((w//10,h//2),resample=Image.ANTIALIAS)
# img.show()