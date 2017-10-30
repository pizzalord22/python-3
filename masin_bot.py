#! python 3
import os
from pyautogui import *
from tkinter import *
import time
import numpy
import pywin32_system32
from PIL import Image
import image as img

img.snapshot()

stat = "agi"


def area1():
    epoch_time_start = int(time.time())
    epoch_time_end = epoch_time_start + 120
    print("start time", epoch_time_start, "end time", epoch_time_end)
    x, y = size()
    x, y = x/2, y/1.7
    time.sleep(3)
    keyDown("1")
    keyUp("1")
    keyDown("1")
    keyUp("1")
    keyDown("up")
    time.sleep(0.75)
    keyUp("up")
    moveTo(x, y, 0.1)
    click(button="right")
    time.sleep(7.5)
    keyDown("right")
    time.sleep(0.75)
    keyUp("right")
    keyDown("a")
    moveTo(x+20, y - 100, 0.1)
    click()
    keyUp("a")
    time.sleep(5)
    keyDown("shift")
    keyDown("a")
    keyUp("a")
    while int(time.time()) < epoch_time_end:
        moveTo(x - 250, y - 100, 0.1)
        click()
        moveTo(x, y - 100, 0.1)
        click()
    keyUp("shift")
    click()
    time.sleep(1)
    print("code run getting stats")
    stats(stat)


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
    area1 = Button(root, text='area 1', width=25, command=area1)
    area1.pack()
    root.mainloop()

