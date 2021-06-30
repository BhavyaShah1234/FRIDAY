import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import pyautogui as pag
import psutil
import pyjokes

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


def speak(audio):
    print(f'FRIDAY:{audio}')
    engine.say(audio)
    engine.runAndWait()


def clock(x, y, z):
    speak(f'The time is {x} hours, {y} minutes and {z} seconds')


def calender(a, b, c, d):
    if b == 1 or b == 21 or b == 31:
        speak(f'Today is {c} {b}st, {d}, a {a}')
    elif b == 2 or b == 22:
        speak(f'Today is {c} {b}nd, {d}, a {a}')
    elif b == 3 or b == 23:
        speak(f'Today is {c} {b}rd, {d}, a {a}')
    else:
        speak(f'Today is {c} {b}th, {d}, a {a}')


def mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL', 'YOUR_PASSWORD')
    server.sendmail('OTHER_EMAIL', to, content)
    server.close()


def insta_bomb():
    speak('Enter number of bombs to be dropped.')
    n = int(listen())
    speak('Enter a phone number.')
    number = listen().lower()
    chrome_options = Options()
    chrome_options.add_argument('headless')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
    for i in range(n):
        browser.get('https://www.instagram.com/accounts/password/reset/')
        WebDriverWait(browser, 5).until(ec.presence_of_all_elements_located((By.NAME, 'cppEmailOrUsername')))
        sleep(5)
        browser.find_element_by_name('cppEmailOrUsername').send_keys(f'+91{number}')
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div[2]/div/div/div[5]/button').click()
        sleep(5)
    browser.quit()
    return False


def cpu():
    usage = str(psutil.cpu_percent())
    speak(f'The CPU has {usage}% utilization')


def battery():
    b = psutil.sensors_battery().percent
    speak(f'The battery is at {b}%')


def jokes():
    joke = pyjokes.get_joke('en', 'neutral')
    speak(joke)


def screenshot():
    img = pag.screenshot()
    img.save(r'C:\Users\user\PycharmProjects\Automation\screenshot.png')


def wish_me():
    h = int(datetime.datetime.now().time().hour)
    if 6 <= h < 12:
        speak('Good morning sir. I am FRIDAY, your personal assistant. How may I help you?')
    elif 12 <= h < 18:
        speak('Good afternoon sir. I am FRIDAY, your personal assistant. How may I help you?')
    elif 18 <= h <= 23:
        speak('Good evening sir. I am FRIDAY, your personal assistant. How may I help you?')
    elif 0 <= h < 6:
        speak('Good night sir. I am FRIDAY, your personal assistant. How may I help you?')


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        user = recognizer.listen(source=source, timeout=20000, phrase_time_limit=20000)
    try:
        print('Recognizing....')
        query = recognizer.recognize_google(user, language='en')
        print(query)
    except Exception as e:
        print(e)
        return 'none'
    return query


if __name__ == '__main__':
    wish_me()
    while True:
        command = listen().lower()
        if 'calender' in command or 'today' in command:
            day = datetime.datetime.today().strftime('%A')
            date = datetime.datetime.now().date().day
            year = datetime.datetime.today().year
            month = datetime.datetime.today().strftime('%B')
            calender(day, date, month, year)
        elif 'clock' in command or 'time' in command:
            hour = datetime.datetime.now().time().hour
            minute = datetime.datetime.now().time().minute
            sec = datetime.datetime.now().time().second
            clock(hour, minute, sec)
        elif "what is your name" in command:
            speak("I am FRIDAY. Mr.Bhavya's personal assistant.")
        elif 'how are you' in command:
            speak('I am a program. I have no physical form. So I am always well.')
        elif 'wikipedia' in command:
            command = command.replace('wikipedia', '')
            result = wp.summary(command, sentences=5)
            speak(f'According to Wikipedia, {result}')
        elif 'send mail' in command or 'email' in command:
            try:
                speak('Whom should I send it to?')
                receiver = input("Enter receiver's email address:")
                speak('What should I say?')
                body = listen().lower()
                mail(receiver, body)
                speak('Email sent successfully.')
            except Exception as a:
                print(a)
                speak('Email send unsuccessful.')
        elif 'search' in command or 'look out' in command:
            speak('What are you looking for?')
            search = listen().lower()
            words = search.split(' ')
            sent = ''
            for i in words:
                sent = sent + '+' + i
            driver = webdriver.Chrome(executable_path=r'PATH')
            driver.get(f'https://www.google.com/search?q={sent}&spell=1&sa=X&ved=2ahUKEwjnqYCcjpTsAhUn4zgGHRdEBV4QBSgAegQIJBAp&biw=1600&bih=789')
        elif 'youtube' in command:
            speak('What should I find?')
            search = listen().lower()
            words = search.split(' ')
            sent = ''
            for i in words:
                sent = sent + '+' + i
            driver = webdriver.Chrome(executable_path=r'PATH')
            driver.get(f'https://www.youtube.com/results?search_query={sent}')
        elif 'drop insta bombs' in command:
            running = True
            while running:
                running = insta_bomb()
        elif 'processor' in command or 'CPU' in command:
            cpu()
        elif 'battery' in command:
            battery()
        elif 'tickle me' in command or 'humor me' in command or 'a joke' in command:
            jokes()
        elif 'word' in command or 'MS Word' in command:
            path = r'PATH'
            os.startfile(path)
        elif 'powerpoint' in command:
            path = r'PATH'
            os.startfile(path)
        elif 'notepad' in command:
            path = r'PATH'
            os.startfile(path)
        elif 'excel' in command:
            path = r'PATH'
            os.startfile(path)
        elif 'paint' in command or 'MS paint' in command:
            path = r'PATH'
            os.startfile(path)
        elif 'make notes' in command or 'take notes' in command:
            speak("What's on your mind?")
            notes = listen()
            file = open('notes.txt', 'w')
            speak('Should I include the time?')
            answer = listen()
            if 'yes' in answer or 'sure' in answer:
                time = str(datetime.datetime.now().strftime("%d %b %Y, %H:%M:%S"))
                file.write(f'{time}:\n    {notes}')
                speak('You are all set sir.')
            elif 'no' in answer or "don't" in answer:
                file.write(f'{notes}')
                speak('You are all set sir.')
        elif 'read my notes' in command:
            speak('Showing notes....')
            file = open('notes.txt', 'r')
            speak(file.read())
        elif 'screenshot' in command:
            screenshot()
        elif 'exit' in command or 'bye friday' in command:
            speak("Goodbye sir.")
            exit(0)
        else:
            speak("I didn't get you sir.")
