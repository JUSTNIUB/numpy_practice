import random
from PIL import Image,ImageDraw,ImageFont

class GenerateCode():
    def getcode(self):
        return chr(random.randint(65,90))
    def bg_color(self):
        return (random.randint(50,160),
                random.randint(50,160),
                random.randint(50,160))
    def fr_color(self):
        return (random.randint(160,255),
                random.randint(160,255),
                random.randint(160,255))
    def gen_pic(self):
        w,h=240,80
        img = Image.new(size=(w,h),mode='RGB',color=(255,255,255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font='inkfree.ttf',size=50)
        for y in range(h):
            for x in range(w):
                draw.point((x,y),fill=self.bg_color())
        for i in range(4):
            draw.text((60*i+20,10),text=self.getcode(),fill=self.fr_color(),font=font)
            draw.rectangle((10,10,70,70))
        img.show()
        img.save("test.jpg")

g = GenerateCode()
g.gen_pic()