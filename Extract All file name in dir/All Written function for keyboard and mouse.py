from re import X
from PIL.ImageOps import posterize
import pyautogui as p
import time

def hit(key):
    return p.keyDown(key)

def move(x, y):
    return p.moveTo(x, y)

def Lc():
    return p.click()

def Rc():
    return p.rightClick()

def pos():
    time.sleep(4)
    pose = p.position()
    return pose

def combo(key1, key2):
    return p.hotkey(key1, key2)

def write(words):
    return p.write(words)
