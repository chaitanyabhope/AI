from asyncio import subprocess
from http import client, server
from random import random
import re
from sys import stdout
from time import time
from unittest import result
from urllib import response
from click import echo_via_pager
from flask import request
from jmespath import search
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import json
import requests
from bs4 import BeautifulSoup

print('Loading your AI personal voice Assistant- G-one')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day =datetime.datetime.today().weekday()+1
    Day_dict ={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}

    if day in Day_dict.keys():
        day_of_the_week= Day_dict[day]
        print(day_of_the_week)
        speak('The day is'+day_of_the_week)


def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am G-one, your personal voice assistant. Please tell me how may I help you")
    print("I am G-one, your personal voice assistant. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again, please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia.., please wait')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=6)
            speak("According to wikipedia")
            print(results)
            speak(results) 

        elif 'which day it is' in query:
            tellDay()

        elif 'what is love' in query:
            speak('It is 7th sense that destroy all other senses')


        elif 'programming languages' in query:
            speak('Programming languages are the most important part of this generations, also our future is mostly depending on It'
            'I know some of the programming languages, that are very important like c, c++, java, python, .net, HTML, CSS and many more'
            'In which i am created using the python language,'
            'If you want to know, more about programming languages, you can command me to open geekforgeeks, javatpoint,W3Oschool,tutorialspoint etc')

        elif 'shutdown system' in query:
            speak("Hold on a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p/f')


        elif 'change name' in query:
            speak("what would you like to call me sir")
            assname = takeCommand()
            speak('Thanks for naming me')

        elif 'career suggestion' in query:
            speak('if you completed your 10th or 12th from a recognised college or if you wanted to get advice, then i will suggest you to'
            'go for the courses or branches which are based on your interest, your interest is most important in this case'
            'or if you want to go for the courses which are based on the technology, computer, artificial intelligence, medical this feilds have the most scope at this situation.')

        elif 'bro' in query:
            speak("yes boss")

        elif 'your age' in query:
            def calculateage(birthdate):
                today = datetime.date.today()
                age = today.year - birthdate.year -((today.month,today.day)<(birthdate.month,birthdate.day))
                return age
                speak(age)
            speak('My age is printed on the screen, i am created in 2022 so my age will be small')
            print(calculateage(datetime.date(2022,1,1)),"years")
            

        elif 'you married' in query:
            speak("marriage is a wedding ceremony in humans but i am a virtual assistant so it is not possible for me.")

        elif 'open geeksforgeeks' in query:
            speak('opening geekforgeeks')
            webbrowser.open('geekforgeeks.org')

        elif 'open javatpoint' in query:
            speak('opening javatpoint')
            webbrowser.open('javatpoint.com')

        elif 'open w3oschool' in query:
            speak('opening w3oschool')
            webbrowser.open('w3oschool.com')

        elif 'open tutorialspoint' in query:
            speak('opening tutorialspoint')
            webbrowser.open('tutorialspoint.com')

        elif 'fine' in query:
            speak("It's good to know that you are fine")

        elif 'your name' in query:
            speak("My friends call me G-one, you can also call me G-One")
            print("My friends call me G-one, you can also call me G-One")

        elif 'who i am' in query:
            speak("If you talk then definately you are human")

        elif "why you came to world" in query:
            speak("I am created by the purpose of assistant which will help you")


        elif 'about you' in query or 'who created you' in query:
            speak(f"I am a virtual voice assistant. Created by 3rd year computer engineering students of Government polytechnic osmanabad. Under the guidance of faculties and honourable head of department Mr. P. J. Bansode sir")

        elif 'who are you' in query or 'what can you do' in query:
            speak("I am G-one version 1 point O your personal assistant. I am programmed to minor tasks like "
            'opening youtube, google, chrome, gmail and stackoverflow, predict time, search wikipedia, predict weather'
            'in different cities, get top headline news from times of india')

        
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak('Opening stackoverflow website, please wait')
            webbrowser.open("https://stackoverflow.com/")

        elif 'open gmail' in query:
            speak('opening gmail, please wait')
            webbrowser.open('www.gmail.com')


        elif 'search' in query:
            speak('what you want to search')
            query4 = takeCommand()
            speak('Here i got something related on web, please wait!')
            results = 'https://www.google.com/search?q='+query4
            webbrowser.open(results)

        elif 'date' in query:
            today= datetime.date.today()
            speak('date of today is')
            speak(today)

        elif 'news' in query:
            speak('searching news on web, please wait... here i got something for you')
            results = webbrowser.open('https://www.google.com/search?q=latest+news')
            time.sleep(5)

        elif 'jokes' in query:
            speak('i am searching jokes on web, please wait... here i got something for you')
            webbrowser.open('https://www.google.com/search?q=funny+jokes')

        elif 'play music' in query:
            speak('here you go with music')
            music_dir = 'C:\\Users\\HP\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir,songs[1]))

        elif 'open pycharm' in query:
            speak('opening the desired application')
            os.system('PyCharm')

        elif 'open notepad' in query:
            speak('opening notepad, please wait')
            os.system('Notepad')

        elif 'open microsoft edge' in query:
            speak('opening edge, please wait')
            os.system('MicrosoftEdge')

        elif 'youtube' in query:
            speak('what you want to search on youtube')
            query1 = takeCommand()
            search = 'https://www.youtube.com/results?search_query='+query1
            speak('I got something related on youtube')
            webbrowser.open(search)

        elif 'location' in query:
            speak('which place you want to search location')
            query2 = takeCommand()
            search = 'https://www.google.com/maps/place/'+query2
            speak('here, I got the location on the map, you can see it on your screen')
            webbrowser.open(search)

        elif 'weather' in query:
            speak('Please,tell city name of which you want to find weather of')
            query1 =takeCommand()
            search='https://www.google.com/search?q=weather+of'+query1
            speak('here, i got result on your screen')
            webbrowser.open(search)
            
        elif 'how are you' in query:
            speak("I am fine, Thank you for asking, sir")
            speak("How are you, Sir") 

        elif 'what is' in query:
            speak('please, repeat what you want to know')
            query1=takeCommand()
            speak('i am searching it on web, please wait a second')
            search='https://www.google.com/search?q=what+is'+query1
            speak('here i got some result')
            webbrowser.open(search)

        elif 'calculate' in query:
            question=takeCommand()
            app_id='VGK94G-4KPYT3EGH2'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).query
            speak('The answer is'+answer)

        elif 'good by' in query:
            speak('ok sir, you can call me anytime!')
            speak('just say wake up g-one')
            break

        elif 'Thanks for your help' in query:
            speak('my pleasure, its good to know that i am helpable for you ')