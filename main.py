import pyttsx3 as p 
import speech_recognition as sr
from testt import *
from test2yt import *
from News import *

import randfacts
from jokes import *
from weather import *
import datetime


engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and  hour<16:
        return("afternoon")
    else:
        return("evening")

today_date=datetime.datetime.now()
r=sr.Recognizer()

speak("Hello sir,good"+wishme()+ "I'm your voice assistant.")
speak("Time is" + today_date.strftime("%d")+"of"+today_date.strftime("%B")+"and its currently"+(today_date.strftime("%I")+(today_date.strftime("%M"))+(today_date.strftime("%p")))) 
speak("Temperature in Varansi is "+ str(temp()) + "degree celsius" + "and with " + str(des()))
speak("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am also having a good day sir")
speak("what can i do for you??")


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text2 = r.recognize_google(audio)


if "information" in text2:
    speak("you need information related to  which topic")
    
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio=r.listen(source)
        infor = r.recognize_google(audio)
    
    
    speak("searching in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)
    
elif "play" and "video" in text2:
    speak("you want me to play which video??")
     
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio=r.listen(source)
        vid = r.recognize_google(audio)
    print("playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)
    
    
elif "news" in text2:
    print("sure sir, now i  will read news for you.")
    speak("sure sir, now i  will read news for you.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
        
        
#elif "fact" or "facts" in text2:
    #speak("sure sir,")
    #x=randfacts.getFact()
    #print(x)
    #speak("Did you know that, "+x)
    
    
elif "joke" or "jokes" in text2:
    speak("sure sir get ready for some chukles")
    arr=joke()
    
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
       
