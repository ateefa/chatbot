# from chatterbot import ChatBot
# chatbot = ChatBot("JIM")
#
#
# while True:
#     request = input('YOU: ')
#     response = chatbot.get_response(request)
#     print('BOT: ',response)
#     if(request == "bye"):
#        break

import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr

import pyowm
engine = pyttsx3.init()

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?', 'how are you']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
        if r.recognize_google(audio) in greetings:
            random_greeting = random.choice(greetings)
            print(random_greeting)
            engine.say(random_greeting)
            engine.runAndWait()
        elif r.recognize_google(audio) in question:
            engine.say('I am fine')
            engine.runAndWait()
            print('I am fine')
        elif r.recognize_google(audio) in var1:
            engine.say('I was made by edward')
            engine.runAndWait()
            reply = random.choice(var2)
            print(reply)
        elif r.recognize_google(audio) in cmd9:
            print(random.choice(repfr9))
            engine.say(random.choice(repfr9))
            engine.runAndWait()
        elif r.recognize_google(audio) in cmd7:
            print(random.choice(colrep))
            engine.say(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            engine.say('It keeps changing every micro second')
            engine.runAndWait()
        elif r.recognize_google(audio) in cmd8:
            print(random.choice(colrep))
            engine.say(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            engine.say('It keeps changing every micro second')
            engine.runAndWait()
        elif r.recognize_google(audio) in cmd2:
            mixer.init()
            mixer.music.load("C:\\Users\Edward Zion SAJI\Downloads\Mighty_God_-_Martin__Colleen_Rebeiro.55145718.wav")
            mixer.music.play()
        elif r.recognize_google(audio) in var4:
            engine.say('I am edza your personal AI assistant')
            engine.runAndWait()
        elif r.recognize_google(audio) in cmd4:
            webbrowser.open('www.youtube.com')
        elif r.recognize_google(audio) in cmd6:
            print('see you later')
            engine.say('see you later')
            engine.runAndWait()
            exit()
        elif r.recognize_google(audio) in cmd5:
            owm = pyowm.OWM('f4b66d9278957434d737978e0712d3b0')
            sf = owm.weather_at_place('Nagpur, IN')
            weather = sf.get_weather()
            temp = "temprature is " + str(weather.get_temperature('fahrenheit')['temp'])
            print(temp)
            engine.say(temp)
            engine.runAndWait()
        elif r.recognize_google(audio) in var3:

            print("Current date and time : ")
            print(now.strftime("The time is %H:%M"))
            engine.say(now.strftime("The time is %H:%M"))
            engine.runAndWait()
        elif r.recognize_google(audio) in cmd1:
            webbrowser.open('www.google.com')
        elif r.recognize_google(audio) in cmd3:
            jokrep = random.choice(jokes)
            engine.say(jokrep)
            engine.runAndWait()
        else:
            engine.say("please wait")
            engine.runAndWait()
            print(wikipedia.summary(r.recognize_google(audio)))
            engine.say(wikipedia.summary(r.recognize_google(audio)))
            engine.runAndWait()
            userInput3 = input("or else search in google")
            webbrowser.open_new('www.google.com/search?q=' + userInput3)
