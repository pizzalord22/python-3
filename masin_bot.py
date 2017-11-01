#! python 3
import os
from pyautogui import *
from tkinter import *
import time
import numpy
import pywin32_system32
from PIL import Image
from PIL import ImageGrab
import image as img

x_pad = 82
y_pad = 104
dead_pixel = x_pad+31, y_pad+39

stat = "agi"


def pres_key(key, sleep_time=0.1, amount=1, delay=0.01):
    for i in range(amount):
        keyDown(key)
        time.sleep(float(sleep_time))
        keyUp(key)
        print(key, "was pressed", i+1, "time(s) for", sleep_time, "with a delay of", delay, "seconds between presses")


def mouse_click(x_coord, y_coord, move_time=0.2, button="left", amount=1):
    moveTo(x_pad+x_coord,y_pad+y_coord, move_time)
    for i in range(amount):
        click(button=button)
    print("moved mouse to x:" + str(x_pad+x_coord), "y:" + str(y_pad+y_coord), "clicked the", button, "mouse button", amount, "times")


def area1():
    # epoch_time_start = int(time.time())
    # epoch_time_end = epoch_time_start + 120
    # print("start time", epoch_time_start, "end time", epoch_time_end)
    time.sleep(3)
    pres_key("1", 0.1, 2)
    pres_key("up", 0.5, 1)
    img.snapshot()
    # moveTo(x, y, 0.1)
    # click(button="right")
    # time.sleep(7.5)
    # keyDown("right")
    # time.sleep(0.75)
    # keyUp("right")
    # keyDown("a")
    # moveTo(x+20, y - 100, 0.1)
    # click()
    # keyUp("a")
    # time.sleep(5)
    # keyDown("shift")
    # keyDown("a")
    # keyUp("a")
    # image = img.snapshot()
    #while image.getpixel(dead_pixel) != (100, 102, 53):
    #    moveTo(x - 250, y - 100, 0.1)
    #    click()
    #    moveTo(x, y - 100, 0.1)
    #    click()
    #    img.snapshot()
    # keyUp("shift")
    # click()
    # time.sleep(1)
    # stats(stat)


def stats(stat):
    keyDown("enter")
    keyUp("enter")
    typewrite("-greed")
    keyDown("enter")
    keyUp("enter")
    keyDown("enter")
    keyUp("enter")
    typewrite("-"+stat)
    keyDown("enter")
    keyUp("enter")
    keyDown("enter")
    keyUp("enter")
    typewrite("-save")
    keyDown("enter")
    keyUp("enter")
    keyDown("enter")
    keyUp("enter")
    typewrite("-suicide")
    keyDown("enter")
    keyUp("enter")


# create an user interface for the bot
def gui():
    root = Tk()
    root.title("Masin bot v1")
    area1_button = Button(root, text='area 1', width=25, command=area1)
    snapshot_button = Button(root, text="snapshot", width=25, command=img.snapshot)
    area1_button.pack()
    snapshot_button.pack()
    root.mainloop()


#gui()

mouse_click(0, 0, 0.2, "left", 1)
