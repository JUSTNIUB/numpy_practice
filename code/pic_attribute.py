from PIL import Image,ImageFilter
import matplotlib.pyplot as plt
img = Image.open(r"myimage/1.jpg")


#show 图片
# img.show()
# plt.figure()
# plt.imshow(img)
# plt.title("earth")
# plt.show()
w,h = img.size
print(w,h)

#缩放图片
# bands = img.getbands()
# print(bands)
# mode = img.mode
# print(mode)
# img = img.resize((w//2,h//2))
# img.show()
#
# #等比缩放
# img.thumbnail((w//2,h//2),resample = Image.ANTIALIAS)
# img.show()

# #抠图
# img = img.crop((100,100,400,400))
# img.show()
#
# #旋转
# img =img.rotate(-90)
# img.show()

#滤波器
# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img = img.filter(ImageFilter.BLUR)
# img.show()
# img = img.filter(ImageFilter.BoxBlur(radius=10))
# img.show()
# img = img.filter(ImageFilter.DETAIL)
# img.show()
# img = img.filter(ImageFilter.EMBOSS)
# img.show()
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()

#加logo
logo = Image.open("myimage/2.jpg")
logo = logo.resize((60,60),resample=Image.ANTIALIAS)
img.paste(logo,(100,100))
img.show()