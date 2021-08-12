import os
from time import sleep
import speech_recognition as sr
from fuzzywuzzy  import fuzz
import pyttsx3
import datetime
import webbrowser as web
from colorama import Fore
import random
import pyautogui
import subprocess
from pyowm import OWM
import getpass
from tkinter import *
import ctypes
from PIL import Image
import keyborad

file = (r'C:\Light\Core\input\Speakinput.txt')
os.system("start "+ file)

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    audio = r.listen(source)
    try:                                      
        query = r.recognize_google(audio, language="ru-RU")
        query = query.lower()+" "
        print(query)
        keyboard.write(str(query),delay=0)
        pg.typewrite(["enter"])
        pg.typewrite('ctrl', 's')
    except sr.UnknownValueError:
        pass