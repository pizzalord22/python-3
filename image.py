from PIL import ImageGrab
from time import *


def snapshot():
    sleep(5)
    for i in range(10):
        img = ImageGrab.grab()
        crop_rectangle = (65+17, 85+19, 1094, 595)
        img = img.crop(crop_rectangle)
        img.save("game"+str(i)+".jpg", "JPEG")
        sleep(5)

