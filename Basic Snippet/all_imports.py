import win32gui
import sys
from pushbullet import Pushbullet 
import re
import win32con
import win32com.client 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pg
import os
from selenium.webdriver.common.alert import Alert
from tempfile import mkstemp
from shutil import move, copymode,make_archive
from os import fdopen, remove
import zipfile
import fnmatch
import random
import xlsxwriter
import subprocess
import requests
import json
from datetime import date

today = date.today()
csv_path = f'D:\Plag\plag({today}).csv'


def getVars(line):
    with open('D:\Plag\Vars.txt','r') as f:
        return f.readlines()[line].removesuffix('\n')
        
try:
    try:
        hWnd = win32gui.FindWindow(None, 'Turnitin - Google Chrome')
        win32gui.BringWindowToTop(hWnd)
    except Exception:
        hWnd = win32gui.FindWindow(None, 'Turnitin - Class Portfolio - Google Chrome')
        win32gui.BringWindowToTop(hWnd)
except Exception as e:
    print(e)
    subprocess.call(f'"D:\Chrome_(8989).bat"') 
    print('=========== Starting {0}.bat ==================='.format(getVars(5)))
 

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
opt = Options()
opt.add_experimental_option("debuggerAddress",f"localhost:8989")
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
try:
    driver = webdriver.Chrome(executable_path=r'C:\Users\Priyam\.wdm\drivers\chromedriver\win32\103.0.5060.134\chromedriver.exe',options=opt)
except Exception:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
plgpath = r'D:\Plag\plagdir'
raw_path = r'D:\Plag\Raw'
block_cipher = None

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf'):
                ziph.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                                           os.path.join(path, '..')))
                try:
                    os.remove(f'{path}\\{file}')
                except Exception as e:
                    print(e)
                print(f'[Result]: {file} has been zipped')
def notify(title, body):
	TOKEN = 'o.4KlKeaBTBMI1yFpISKAVxjDuHlfSdEv6' 
	msg = {"type": "note", "title": title, "body": body}
	resp = requests.post('https://api.pushbullet.com/v2/pushes',
						data=json.dumps(msg),
						headers={'Authorization': 'Bearer ' + TOKEN,
								'Content-Type': 'application/json'})
	if resp.status_code != 200: # Check if fort message send with the help of status code
		raise Exception('Error', resp.status_code)
	else:
		print('[Info]: Message sent')

def get_last_msg():
    TOKEN = 'o.4KlKeaBTBMI1yFpISKAVxjDuHlfSdEv6' 
    pb = Pushbullet(TOKEN) 
    pushes = pb.get_pushes() 
    latest = pushes[0]
    pb.delete_push(latest.get("iden")) 
    return str(latest['body']).capitalize()
    
def tab(n):
    tn = driver.window_handles[n]
    driver.switch_to.window(tn)

def Wait(xpth):
    return WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpth)))

def findxpth(xpath):
    try:
        return driver.find_element(by=By.XPATH,value=xpath)
    except Exception:
        pass


def extract_Zip():
    for dirpath, dirs, files in os.walk(raw_path):
            for filename in files:
                try:
                    if filename.endswith('.zip') or filename.endswith('.rar') :
                        file_name = f'{dirpath}\\{filename}'
                        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                        zip_ref.extractall(raw_path) # extract file to dir
                        zip_ref.close() # close file
                        os.remove(file_name) # delete zipped file
                        print('[INFO]',file_name,'Zip file extracted')
                    else:
                        print('No Zip or rar file found')
                except Exception as e:
                    print('Exception in extract zip: ',e)

def remove_emty_folder():
    folders = list(os.walk(raw_path))[1:]
    for folder in folders:
        # folder example: ('FOLDER/3', [], ['file'])
        if not folder[2]:
            os.rmdir(folder[0])
            
def move_all_doc():
    extract_Zip()
    for dirpath, dirs, files in os.walk(raw_path):
        for filename in files:
            if filename.endswith('.docx'):
                move(f'{dirpath}\\{filename}',f'{plgpath}\\{filename}')
def writVar(cont):
    try:
        with open('data.csv','a',encoding="utf-8") as f:
            f.write(f'{cont}')
            f.close()
    except Exception:
        pass

def writData():
    workbook = xlsxwriter.Workbook('hello.xlsx','a')
    worksheet = workbook.add_worksheet() 
    worksheet.write('A1', 'Hello..')
    workbook.close()