import numpy as np
from PIL import Image


img = Image.open("myimage/1.jpg")
img = img.crop((0,0,400,400))
img.show()

data = np.array(img)
w,h,c = data.shape

# data = data.reshape(4,w//2,h//2,c)
data = data.reshape(2,w//2,2,h//2,c)
data = data.transpose(0,2,1,3,4)
data = data.reshape(4,w//2,h//2,c)
for i in range(4):
    img = Image.fromarray(data[i])
    img.show()