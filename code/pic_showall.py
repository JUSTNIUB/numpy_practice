from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

imagepath = os.listdir("myimage")
print(imagepath)

for i in imagepath:
    imagedir = 'myimage/'+i
    pic = Image.open(imagedir)
    plt.imshow(pic)
    plt.title(i)
    plt.show(block=False)
    plt.pause(1)
    plt.close()