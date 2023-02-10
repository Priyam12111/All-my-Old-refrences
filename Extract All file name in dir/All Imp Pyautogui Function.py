import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    return pyautogui.keyDown(key)

def move(x, y):
    return pyautogui.moveTo(x, y)

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

def click():
    return pyautogui.click()

def pos():
    time.sleep(2)
    pose = pyautogui.position()
    return pose

def drag(x, y,duration):
    return pyautogui.drag(x, y, duration)


# Now, Functions are ready to call just call them.
# a = pos()
# print(a)

