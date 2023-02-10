import shutil
import ctypes
import win32gui
import win32com.client 
import time
import os
import win32com.client 
import time
from re import I
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pg
import os
from selenium.webdriver.common.alert import Alert
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

block_cipher = None
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"#It Stop the page Loading
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
opt.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
csv_path = 'D:\Plag\plag.csv'

def fg(cls,fle):
    shell = win32com.client.Dispatch('WScript.Shell')
    hwnd = win32gui.FindWindow(None, cls)
    win32gui.ShowWindow(hwnd,5)
    win32gui.SetForegroundWindow(hwnd)
    shell.SendKeys(f'{fle}')
    # shell.SendKeys('{Down}')
    shell.SendKeys('{Enter}')

driver.find_element(by=By.XPATH,value=f'//*[@id="choose-file-btn"]').click()
path = os.listdir('D:\Plag\plagdir')[0]
time.sleep(4)
fg('open',path)