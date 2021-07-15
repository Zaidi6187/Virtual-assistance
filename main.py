import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import requests,json
import googletrans
from pygame import * #for songs
import pyautogui
import sounddevice
from scipy.io.wavfile import write

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def graphics():
    os.system('start C:\\Users\\ykris\\Desktop\\Jarvis\\Rainmeter')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18: 
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")    

def takeCommand():
    # It takes microphone input from the user and returns string output
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     speak("listening ...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)

    # try:
    #     print("Recognizing...")    
    #     query = r.recognize_google(audio, language='en-in')
    #     print(f"User said: {query}\n")

    # except :

    #     print("Say that again please...")  
    #     query= "None"
    query = input("Give Command sir  ")
    return query

def online():
    speak("hello sir.....,starting all systems applications...,installing all drivers")
    
    speak("every driver is installed...,all system have been started")
    speak('ready to work for you...')

def dt():
    strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    print(f"Sir, the date and time is {strTime}")
    speak(f"Sir, the date and time is {strTime}")


def weather():
    url="http://api.openweathermap.org/data/2.5/weather?appid=02d38abc78cb349fa50e383a63becb90&q=Delhi"
    response=requests.get(url)
    x=response.json()
    if x["cod"] != "404" :
        y = x["main"]
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"]
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +  
              "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
               "\n humidity (in percentage) = " +
                    str(current_humidiy) +
               "\n description = " +
                    str(weather_description)) 
        speak(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
              " atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
               " humidity (in percentage) = " +
                    str(current_humidiy) +
               " description = " +
                    str(weather_description))  

def translator():
    speak("tell me sentence please..")
    from googletrans import Translator
    text = takeCommand()
    translator= Translator()
    speak("In which language you want to translate ...")
    m=takeCommand()
    key=m.lower()

    if 'french' in key:
        translation = translator.translate(text, dest='fr')
        print (translation.text)
        speak(translation.text)

    elif 'latin' in key:
        translation = translator.translate(text, dest='la')
        print (translation.text)
        speak(translation.text)

    elif 'italian' in key:
        translation = translator.translate(text, dest='it')
        print (translation.text)
        speak(translation.text)

    elif 'german' in key:
        translation = translator.translate(text, dest='de')
        print (translation.text)
        speak(translation.text)

    elif 'hindi' in key:
        translation = translator.translate(text, dest='hi')
        print (translation.text)
        speak(translation.text)
        
def screenshot():
    iml=pyautogui.screenshot()
    iml.save('C:\\Users\\LENOVO\\OneDrive\\Pictures\\Screenshots')
    speak("Screenshot taken ..let me to show you the screenshot ..")
    os.startfile('C:\\Users\\LENOVO\\OneDrive\\Pictures\\Screenshots')

def email():
    try:
        print("Whom you want to send email.?")
        speak("Whom you want to send email.?")
        a=takeCommand().lower()
        if 'krishna' in a:
            to = "imkmyadav@gmail.com" 
            speak("What should I say?")
            content = takeCommand()   
            sendEmail(to, content)
            
        elif 'hussain' in a:
            to='hussainzaidi86967@gmail.com'
            speak("What should I say?")
            content = takeCommand()   
            sendEmail(to, content)
            

    except Exception as e:
        print(e)
        speak("Sorry sir. I am not able to send this email")    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saniyazaidi39@gmail.com', 'Yaali@123')
    server.sendmail('hussainzaidi86967@gmail.com', to, content)
    server.close()
    speak("Email has been sent!")

def youtube():
    speak("opening youtube ,.. what do you want to play ...")
    a=takeCommand()
    b=a.lower()
    if 'favourite' in b:
        speak("playing your favourite videos.. enjoy video...?")
        print("playing your favourite videos ...enjoy video...")
        url = "https://www.youtube.com/watch?v=jzD_yyEcp0M"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak('enjoy')

    elif 'punjabi' in b:
        speak("playing your punjabi videos.. enjoy video..")
        print("playing your punjabi videos.. enjoy video..")
        url = "https://www.youtube.com/watch?v=RKioDWlajvo"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak('enjoy')
                    
    elif 'english' in b:
        speak("playing your english videos.. enjoy video..")
        print("playing your english videos.. enjoy video..")
        url = "https://www.youtube.com/watch?v=YqeW9_5kURI&list=PLgLEW2YF9Ey_mL4oeL7kZVxqFS-iBjBJv"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak('enjoy')
                    
    elif 'bollywood' in b:
        speak("playing your bollywood videos.. enjoy video..")
        print("playing your bollywood videos.. enjoy video..")
        url = "https://www.youtube.com/watch?v=YqeW9_5kURI&list=PLgLEW2YF9Ey_mL4oeL7kZVxqFS-iBjBJv"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak('enjoy')

    elif 'tamil' in b:
        speak("playing your tamil videos.. enjoy video..")
        print("playing your tamil videos.. enjoy video..")
        url = "https://www.youtube.com/watch?v=9LmTxCYcBKU"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak('youtube closed')

def google():
    speak("opening google sir,.. do you want to search something. ")
    b=takeCommand().lower()
    if 'yes' in b:
        speak("what do you want search..?")
        print("what do you want search..?")
        new=2
        url="https://en.wikipedia.org/wiki/Python_(programming_language)"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        c=takeCommand()
        webbrowser.get(chrome_path).open(url+c, new=new)
        speak('here it is')

    elif 'no' in b:
        speak("ok sir..")
        url="www.google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak('google chrome closed')
                 
def conditions():
    while True:
        query = takeCommand().lower()
        if 'hello jarvis' in query:
            speak("hello .., give some command sir i am listing..")
            print("hello .., give some command sir i am listing..")

        elif 'go offline'in query:
            quit()
            speak("Thank you..., sir closing all systems...,disconnecting from servers...,going offline now.")
            break  

        elif 'thank you' in query:
            speak("It's my pleasure sir.")  
            print("It's my pleasure sir.")   

        elif 'how are you' in query:
            speak("i am fine sir ..i am enjoying my job..i hope you are also fine.")
            print("i am fine sir ..i am enjoying my job..i hope you are also fine.")

        elif 'your features' in query:
            speak("sir i am a A.I based software code by using python language...and i am still upgrading day by day.I have various features.")
            speak("Some basic features are Speech recognization.., weather forecast...,even i can open google and search in it..,and also i can open your gmail,whatsapp,instagram")
            speak("for your entertainment i can play music as per your choice , play youtube videos and even play movies..")
            speak("and even i can open most of the application softwer present in your computer like notepad.. , powerpoint...., excel ,...word ...etc..")

        elif 'punjabi videos' in query:
            speak("wait sir i am playing some bold punjabi videos for you...")
            speak("Yooo.. lets go bro..")
            url = 'https://www.youtube.com/watch?v=GgmFC8y8q3k'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open my picture' in query:
            os.startfile('C:\\Users\\LENOVO\\OneDrive\\Desktop\\final project\\DSCF2338.JPG')
            speak("Zaidi here its your picture")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            youtube()

        elif 'open google' in query:
            google()
                
        elif 'open gmail' in query:
            url = "gmail.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("opening gmail sir")
            webbrowser.get(chrome_path).open(url)
            speak("you have got some new mails sir")    
        
        elif 'open reddit' in query:
            url = "reddit.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("opening reddit sir")
            webbrowser.get(chrome_path).open(url)
            speak(" reddit opened sir")

        elif 'open whatsapp' in query:
            url = "web.whatsapp.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("opening web whatsapp sir")
            webbrowser.get(chrome_path).open(url)
            speak(" web whatsapp  sir") 

        elif 'open instagram' in query:
            url = "instagram.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("opening insta sir") 
            webbrowser.get(chrome_path).open(url)
            
        elif 'play music' in query:
            speak("ok sir...,starting required application..")
            speak("What do you want me to play for you...")
            print("What do you want me to play for you...")
            k=takeCommand().lower()
            speak("ok sir playing" + k + "for you")

            mixer.init()
            mixer.music.load(k+'.ogg')
            mixer.music.play()

            while mixer.music.get_busy():
                k=takeCommand().lower()
                time.Clock().tick(10)
                if 'song' in k:
                    break

                elif "close" in k:
                    mixer.music.stop()
                    speak("music stopped sir..")
                    break    

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
            

        elif 'date and time' in query:
            dt()

        elif 'weather report' in query:
            speak("wait sir telling weather report...")
            weather()

        elif 'command prompt' in query:
            codePath = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\final project\\jarvis2.py\\main.py"
            os.startfile(codePath)

        elif 'take screenshot' in query:
            screenshot()
        
        elif 'translate language' in query:
            speak("Translating sir")
            translator()

        elif 'send email' in query:
            email()

        elif 'notepad' in query:
            os.startfile('C:\\Windows\\System32\\notepad')
            speak('opening notepad ...')
            
        elif 'powerpoint' in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016')
            speak('opening powerpoint ...')

        elif 'word' in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016')
            speak('opening word ...') 

        elif 'excel' in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2016')
            speak('opening excel ...')

        elif 'record audio' in query:
            fs=44100
            second =10
            print('recording....')
            speak('recording voice ...')
            record_voice=sounddevice.rec(int(second * fs) , samplerate=fs, channels=2)
            sounddevice.wait()
            write('output.wav' ,fs , record_voice)
            print("voice recorded...")
            # speak('do you want to listen the recording...')
            a= takeCommand().lower()
            if 'yes' in a:
                speak('playing recording...')
                mixer.init()
                mixer.music.load('output.wav')
                mixer.music.play()

                while mixer.music.get_busy():
                    time.Clock().tick(10)

            else:
                print("ok sir...")
                speak("ok sir...")        

#main program start here.. 

speak("Initializing Jarvis...")
graphics()
wishMe()
online()
dt()
conditions()
