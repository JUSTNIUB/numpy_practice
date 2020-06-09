import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random
#动态显示

# imgpath = os.listdir("myimage")
# print(imgpath)

# plt.ion()
# for sngpath in imgpath:
#     img = Image.open(f"myimage/{sngpath}")
#     plt.imshow(img)
#     plt.pause(1)
#
# plt.ioff()
# plt.show()
#静态显示
# for sngpath in imgpath:
#     img = Image.open(f"myimage/{sngpath}")
#     plt.imshow(img)
#     plt.show(block=False)
#     plt.pause(1)
    # plt.close()


#创建画板
# fig = plt.figure()
#创建3D对象
# ax = Axes3D(fig)
# x = np.random.randn(100)
# y = np.random.randn(100)
# z = np.random.randn(100)
# x = np.random.normal(10,20,100)
# y = np.random.normal(10,20,100)
# z = np.random.normal(10,20,100)
# ax.scatter(x,y,z,s=10,c='r',marker='v',label='boy')
# plt.legend()
# plt.show()

#图片滤波操作
# img = Image.open('myimage/1.jpg')
# img.show()
# r,g,b = img.split()
# img = Image.merge('RGB',(r.point(lambda x:x==x*0),
#                          g.point(lambda x:x==x*0),
#                          b))
# img.show()

# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()
# img=img.crop((10,10,400,400))
# img.show()
# img=img.rotate(45)
# img.show()
# w,h=img.size
# logo = Image.open('myimage/1.jpg')
# logo = logo.resize((w//5,h//12),resample=Image.ANTIALIAS)
# logo.thumbnail((w//5,h//12),resample=Image.ANTIALIAS)
# img.paste(logo,(20,30))
# img.show()

# class vrfcode():
#     def __init__(self):
#         pass
#     def genChar(self):
#         return chr(random.randint(65,90))
#     def bgColor(self):
#         return (random.randint(0,155),
#                 random.randint(0,155),
#                 random.randint(0,155))
#     def frColor(self):
#         return (random.randint(120,255),
#                 random.randint(120,255),
#                 random.randint(120,255))
#     def genPic(self):
#         w,h=400,100
#         #创建画布
#         new = Image.new(mode='RGB',size=(w,h),color=(0,0,0))
#         #创建画笔
#         draw = ImageDraw.Draw(new)
#         #创建字体
#         font = ImageFont.truetype(size=70,font='Inkfree.ttf')
#         for i in range(w):
#             for j in range(h):
#                 draw.point(xy=(i,j),fill=self.bgColor())
#         for i in range(4):
#             draw.text(font=font,xy=(i*80+30,15),text=self.genChar(),fill=self.frColor())
#         new.save("hello.jpg")
#         new.show()
#
# tsVfcd = vrfcode()
# tsVfcd.genPic()

