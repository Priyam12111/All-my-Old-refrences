import win32gui
import win32con
from time import sleep

sleep(1)

Minimize = win32gui.FindWindow(None, 'Search | Sales Navigator - Google Chrome')
win32gui.BringWindowToTop(Minimize)