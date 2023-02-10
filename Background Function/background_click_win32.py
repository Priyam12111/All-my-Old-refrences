import win32gui
import win32api
import win32con
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui as pg
import time


def pgpost():
    pg.displayMousePosition() 

def name():
    time.sleep(2)
    print(GetWindowText(GetForegroundWindow()))
    return GetWindowText(GetForegroundWindow())

def click(x, y):
    hWnd = win32gui.FindWindow(None, name())

    print(hWnd)
    lParam = win32api.MAKELONG(x, y)

    win32api.SendMessage(hWnd, win32con.WM_KEYDOWN, 0x41, lParam)
    win32api.SendMessage(hWnd, win32con.WM_KEYUP, 0x41, lParam)


# pgpost()
click(211,120)