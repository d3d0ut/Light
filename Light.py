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
import keyboard

banner1 = (''' _     ___ ____ _   _ _____
| |   |_ _/ ___| | | |_   _|
| |    | | |  _| |_| | | |
| |___ | | |_| |  _  | | |
|_____|___\____|_| |_| |_|
''')

banner2 = (''' _ _       _     _
| (_) __ _| |__ | |_
| | |/ _` | '_ \| __|
| | | (_| | | | | |_
|_|_|\__, |_| |_|\__|
     |___/
''')

banner3 = ('''    __    _       __    __
   / /   (_)___ _/ /_  / /_
  / /   / / __ `/ __ \/ __/
 / /___/ / /_/ / / / / /_
/_____/_/\__, /_/ /_/\__/
        /____/
''')

banner4 = ('''    __    ____________  ________
   / /   /  _/ ____/ / / /_  __/
  / /    / // / __/ /_/ / / /
 / /____/ // /_/ / __  / / /
/_____/___/\____/_/ /_/ /_/
''')

banner5 = ('''    ___       __    __
   / (_)___ _/ /_  / /_
  / / / __ `/ __ \/ __/
 / / / /_/ / / / / /_
/_/_/\__, /_/ /_/\__/
    /____/
''')

os.system("cls")
print(Fore.YELLOW)
a = [banner1, banner2, banner3, banner4, banner5]
c = random.choice(a)
print(c)
print(Fore.GREEN)


opts = {
    "alias": ('лайт', 'light', 'пожалуйста', 'прислужник', 'открой', 'покажи', 'включи', 'доброе', 'добрый'
              'сегодняшний', 'дубина','скажи', 'сколько', 'код', 'добавь', 'выключи', 'ты', 'кот', 'поменяй', 'очисти', 'сделай'
              'терра', 'записывай', 'за', 'на', 'сверни', 'верни', 'сделай', 'сделать', 'кликни', 'наклейки', 'компьютер'
              'голосовой', 'закрой', 'выруби', 'жукова'),

    "tbr": ('скажи','расскажи','покажи','сколько','произнеси', 'кэра', 'kara', 'пожалуйста'),
    "cmds": {


        # Light
        "clear": ('очисти историю команд', 'очисти мою историю', 'очисти команды', 'историю команд', 'мою историю', 'команды'),


        # Music
        "music": ('включи мой плейлист', 'мой плейлист'),
        "musicran": ('включи рандомную музыку', 'включи случайную музыку', 'включи рандомную песню', 'включи случайную песню'
            'рандомную музыку', 'случайную музыку', 'рандомную песню', 'случайную песню'),


        # Browser
        "search": ('открой свой поисковик', 'открой мой поисковик', 'мой поисковик', 'свой поисковик'),
        "youtube": ('открой youtube', 'открой ютуб', 'youtube'),
        "browser": ('открой браузер', 'браузер', 'открой основной браузер', 'основной браузер'),
        "animego": ('открой сайт по просмотру аниме', 'открой animego', 'открой сайт аниме', 'сайт по просмотру аниме'
            'animego', 'сайт аниме'),
        "wikipedia": ('открой сайт wikipedia', 'открой wikipedia', 'сайт wikipedia', 'wikipedia', 'википедию', 'открой википедию'),
        "whatsapp": ('открой whatsapp', 'whatsapp', 'ватсапп', 'открой ватсапп'),
        "twitch": ('открой твич', 'твич', 'открой twitch', 'twitch'),
        "virustotal": ('открой virustotal', 'virustotal', 'вирус тотал', 'открой вирус тотал'),
        "gmail": ('открой gmail', 'gmail', 'гмаил', 'открой гмаил'),
        "vk": ('открой вк', 'вк', 'открой vk', 'vk'),
        "googletranslate": ('открой переводчик', 'переводчик', 'открой гугл переводчик', 'гугл переводчик', 'google переводчик', 'октрой google переводчик'),


        # Speak
        "hello": ('привет', 'здарова', 'ку'),
        "bye": ('пока', 'до встречи', 'иди в жопу'),
        "whoareyou": ('кто ты', 'кто вы', 'что ты такое', 'что ты сдесь делаешь'),
        "why": ('почему ты здесь', 'для чего ты здесь'),
        "ctime": ('текущее время','сейчас времени','который час', 'скажи время', 'сколько сейчас времени'),
        "sun": ('утро', 'доброе утро'),
        "today": ('день', 'добрый день'),
        "omw": ('сегодняшний прогноз погоды', 'прогноз погоды'),
        #"you": ('ты лох', 'ты чмо', 'ты говноед', 'ты дебил', 'ты бот', 'ты нуб', 'лох', 'чмо', 'говноед', 'дебил', 'бот', 'нуб'),
        "shut": ('выключи компьютер', 'выключи комп', 'компьютер', 'комп'),
        "work": ('за работу', 'на чём мы остановились', 'работу', 'чём мы остановились'),


        # System
        "startandstop": ('стоп', 'остановись', 'останови видео', 'старт', 'запусти', 'запусти видео'),
        "fullscreen": ('сделай видео полноэкранным', 'полноэкранным', 'сделай полный экран', 'полный экран', 'сделать видео полный экран', 'видео полный экран'),
        "scan": ('просканируй компьютер', 'просканируй комп', 'поищи модификации windows'),
        "cmd": ('открой cmd', 'открой цмд', 'открой командную строку', 'cmd', 'командную строку', 'цмд', 'центр'),
        "scandisk": ('просканируй диск', 'найди угрозы на диск', 'просканируй жёсткий диск'),
        "startup": ('открой папку автозагрузки', 'папку автозагрузки'),
        "window": ('сверни все окна', 'верни окна назад', 'сверни окна', 'верни окна', 'сверни окно', 'верни окно', 'все окна', 'окна назад', 'окна'),
        "click": ('кликни', 'клик', 'сделай клик', 'клик мышкой', 'сделай клик мышкой', 'кликни мышкой', 'мышкой'),
        "rec": ('записывай всё', 'записывай то что слышишь'),
        "stop": ('стоп', 'старт', 'включи видео', 'останови видео', 'возобнови видео', '100', 'топ'),
        "sleep": ('засни', 'спи', 'усни', 'спящий режим'),
        "input": ('голосовой ввод', 'ввод', 'голосовая клавиатура', 'клавиатура'),
        "process": ('закрой все процессы', 'выключи все процессы', 'все процессы', 'выруби все процессы'),


        # Explorer
        "source": ('открой свой исходный код', 'покажи свой исходный код', 'открой свой код', 'покажи свой код'),
        "autorun": ('открой папку автозагрузки', 'покажи папку автозагрузки'),
        "explorer": ('открой проводник', 'покажи проводник', 'проводник'),
        "downloads": ('открой папку загрузки', 'покажи папку загрузки'),
        "temp": ('открой временные файлы', 'открой папку temp', 'покажи временные файлы', 'покажи папку temp', 'погода', 'темп', 'открой темп'),
        "programm": ('открой папку проги', 'папку проги', 'папку с программами'),
        

        # Programm
        "telegram": ('открой телеграм', 'telegram', 'телегу'),
        "discord": ('открой дискорд', 'открой дс', 'discord', 'дс'),
        "memreduct": ('открой мем редакт', 'открой mem reduct', 'дебридат', 'мем редакт'),
        "sublimetext": ('открой редактор кода', 'редактор кода', 'открой согласен текст', 'согласен текст', 'открой саблайм текс', 'саблайм текс'),


        # Коды запуска
        "hot": ('113', 'код 113'),
        "zero": ('718', 'код 718'),
    }
}

# функции
def speak(what):
    print( what )
    engine = pyttsx3.init()
    engine.say( what )
    engine.runAndWait()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print(Fore.GREEN)
        print("[log] Распознано: "+ voice)
    
        if voice.startswith(opts["alias"]):
            cmd = voice
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(Fore.RED)
        x = ["[log] Неизвестная ошибка, проверьте интернет!", "[log] Пожалуйста провертьте подлючение к интернету", "[log] Проверьте подключение к интернету!"]
        c = random.choice(x)
        print(с)
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    # Kara
    elif cmd == 'clear':
        os.system("cls")


    # Music
    elif cmd == 'music':
        web.open('https://www.youtube.com/playlist?list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT')

    elif cmd == 'musicran':
        z = ["https://www.youtube.com/watch?v=XzfWbi9xkgs&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=1",
            "https://www.youtube.com/watch?v=lrgQwvYAIC4&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=2",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=3",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=4",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=5",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=6",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=7",]
        x = random.choice(z)
        web.open(x)


    # Browser
    elif cmd == 'search':
        file = (r'C:/Light/Core/internet.py')
        os.system("start "+ file)

    elif cmd == 'youtube':
        web.open("www.youtube.com")

    elif cmd == 'browser':
        web.open("www.google.com")

    elif cmd == 'animego':
        web.open("https://animego.org/")

    elif cmd == 'wikipedia':
        web.open("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    elif cmd == 'whatsapp':
        web.open("https://www.whatsapp.com/")

    elif cmd == 'twitch':
        web.open("https://www.twitch.tv/")

    elif cmd == 'virustotal':
        web.open("https://www.virustotal.com/gui/home/upload")

    elif cmd == 'gmail':
        web.open("https://mail.google.com/mail/u/0/#inbox")

    elif cmd == 'vk':
        web.open("https://vk.com/feed")

    elif cmd == 'googletranslate':
        web.open("https://translate.google.com/")


    # Speak
    elif cmd == 'hello':
        z = ["Рада снова вас слышать!", 'Что вам угодно?', 'Привет. Чем-нибудь помочь?']
        x = random.choice(z)
        speak(x)

    elif cmd == 'bye':
        z = ["До свидание", 'Не забывайте про меня, пока', 'Удачного дня!', 'Надеюсь что мы снова встретимся']
        x = random.choice(z)
        speak(x)
        quit()

    elif cmd == 'whoareyou':
        speak("Я умная машина который слушет ваши команды. Меня создали чтобы служить вам")

    elif cmd == 'why':
        z = ["Вы скачали меня", "Вы установили меня"]
        x = random.choice(z)
        speak(x)

    elif cmd == 'sun':
        z = ["Доброе утро", 'Доброе. Что вам угодно?', 'Привет. Чем-нибудь помочь?']
        x = random.choice(z)
        speak(x)

    elif cmd == 'owm':
        owm = OWM('4178417d595eb066c767225c216a790c')

        while True:
            try:
                place = input('Выбирите город: ')
                monitoring = owm.weather_manager().weather_at_place(place)
                weather = monitoring.weather
                status = weather.detailed_status
                print(f'It is {status} in {place} now.')
                break
            except:
                pass

    elif cmd == 'you':
        x = ['Обзываться плохо!', 'Иди в жопу', 'Сам такой']
        z = random.choice(x)
        speak(z)

    elif cmd == 'shut':
        x = ['Иди в жопу', 'Сам выключись', 'Пошёл на фиг']
        z = random.choice(x)
        speak(z)

    elif cmd == 'work':
        file = (r'C:\Проги\Sublime_Text 3\sublime_text.exe')
        os.system("start "+ file)


    # System
    elif cmd == 'startandstop':
        pg.typewrite(["space"])

    elif cmd == 'fullscreen':
        pg.typewrite(["F"])

    elif cmd == 'cmd':
        os.system("start")

    elif cmd == 'scan':
        os.system("sfc /scannow")

    elif cmd == 'startup':
        pass

    elif cmd == 'click':
        pg.click()

    elif cmd == 'rec':
        file = (r'C:\Light\Rec\rec.py')
        os.system("start "+ file)

    elif cmd == 'stop':
        pg.typewrite(["space"])

    elif cmd == 'sleep':
        os.system("rundll32 powrprof.dll,SetSuspendState 0,1,0")

    elif cmd == 'window':
        pg.typewrite("win", "D")

    elif cmd == 'input':
        file = (r'C:\Light\Core\input\input.py')
        os.system("start "+ file)

    elif cmd == 'process':
        os.system("taskkill /FI “USERNAME eq SAMURAI” /F")


    # Explorer
    elif cmd == 'temp':
        os.system("start temp")

    elif cmd == 'source':
        file = (r"C:/Light")
        os.system("start "+file)

    elif cmd == 'explorer':
        os.system("start explorer")

    elif cmd == 'downloads':
        os.system("start downloads")

    elif cmd == 'autorun':
        file = (r'C:\Users\SAMURAI\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup')
        os.system("start "+file)


    # Programm
    elif cmd == 'telegram':
        file = (r'C:\Проги\Telegram_Desktop\Telegram.exe')
        os.system("start "+ file)
        
    elif cmd == 'discord':
        file = (r'C:\Users\SAMURAI\AppData\Local\Discord\app-1.0.9002\Discord.exe')
        os.system("start "+ file)

    elif cmd == 'memreduct':
        file = (r'C:\Проги\64\memreduct.exe')
        os.system("start "+ file)

    elif cmd == 'sublimetext':
        file = (r'C:\Проги\Sublime_Text 3\sublime_text.exe')
        os.system("start "+ file)


    # Коды запуска
    elif cmd == 'hot':
        os.system("shutdown -s")

    elif cmd == 'zero':
        os.system("shutdown -r -t 0")


    else:
        x = ["Что вы сказали?", "Я не поняла", "Повторите пожалуйса", "Команда не распознана, повторите", "Я прослушала", "Повтори"]
        c = random.choice(x)
        print(c)

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()
 
stop_listening = r.listen_in_background(m, callback)
while True: sleep(0.1)