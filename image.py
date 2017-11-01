from PIL import ImageGrab
from PIL import Image
from time import *
from datetime import datetime

# x_pad is the x coordinate where the game screen starts
# y_pad is the y coordinate where the game screen starts
# all the coordinates are based on a 1009x by a 488y game screen
# rgb color when dead 100, 102, 53
x_pad = 82
y_pad = 104
dead_pixel = x_pad+31, y_pad+39


def snapshot():
    sleep(1)
    img = ImageGrab.grab()
    crop_rectangle = (x_pad, y_pad, x_pad+1010, y_pad+489)
    img = img.crop(crop_rectangle)
    img.save("images/snapshot_"+str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))+".jpg", "JPEG")
    print("snapshot taken")
    return img


