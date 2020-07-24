import pyttsx3
import datetime
import pyaudio
import wikipedia
import speech_recognition as sr
import os
import webbrowser
import pyfiglet
#-------------------------------------------------------------------------#
engine = pyttsx3.init()
def say(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    recg = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = recg.listen(source)
    try:
        print('Recognizing...')
        command = recg.recognize_google(audio)
        print(f'{command}\n')
    except Exception:
        print('Not found\n')
        print('Please say that again...')
        say('Please say that again...')
        return "None"
    return str(command)
def wish_me(name):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say(f'Good Morning {name} how may I help you')
        print(f'Good Morning {name} how may I help you')
    elif 12 <= hour < 16:
        say(f'Good Afternoon {name} how may I help you')
        print(f'Good Afternoon {name} how may I help you')
    elif 16 <= hour < 21:
        print(f'Good Evening {name} how may I help you')
        say(f'Good Evening {name} how may I help you')
    else:
            print('Sorry, I don\'t work at night. You can use me anytime between 00:00 and 21:00 hrs')
            say('Sorry, I don\'t work at night. You can use me anytime between 00:00 and 21:00')
            say('Have a Good Night')
            del takeCommand

            
banner = pyfiglet.figlet_format("Assistant")
print(banner)
wish_me('Manas')
listening = True
while listening:
    command = takeCommand().lower()
    if 'wikipedia' in command:
        say('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        say("Wikipedia says")
        print(result)
        say(result)
    elif 'open youtube' in command:
        say('Opening Youtube...')
        webbrowser.open('https://www.youtube.com')
    elif 'open google' in command:
        say('Opening Google...')
        webbrowser.open('https://www.google.com')
    elif 'open facebook' in command:
        say('Opening Facebook...')
        webbrowser.open('https://www.facebook.com')
    elif 'open instagram' in command:
        say('Opening Instagram...')
        webbrowser.open('https://www.instagram.com')
    elif 'open twitter' in command:
        say('Opening Twitter...')
        webbrowser.open('https://www.twitter.com')
    elif 'play music' in command:
        say('PLaying Music...')
        music_dir = 'C:\\Users\\manas\\OneDrive\\Desktop\\Muzic'
        muzic = os.listdir(music_dir)
        print(f'playing {muzic} \n')
        os.startfile(os.path.join(music_dir, muzic[0]))
    elif 'the time' in command:
        time = str(datetime.datetime.now().strftime("%H:%M:%S"))
        print(time)
        say(time)
    elif 'shut down' in command:
        print('Shutting Down...')
        say('Shutting Down...')
        os.system('shutdown /s /t 2')
    elif 'reboot' in command or 'restart' in command:
        say('Restarting...')
        print('Restarting...')
        os.system('shutdown /r /t 2')
    elif 'just cause' in command:
        say('Opening Just Cause')
        os.startfile("X:\\Program Files (x86)\\Just Cause 3\\JustCause3.exe")
    elif 'shut up' in command or 'stop talking' in command or 'exit' in command:
        say('Exiting')
        listening = False
    elif 'manas' in command:
        say('manas is my creator')
    elif 'witcher' in command:
        say('opening witcher 3')
        print('Opening Witcher 3...')
        os.startfile('‪X:\\GOG Games\\The Witcher 3 - Wild Hunt\\bin\\x64\\witcher3.exe')
    elif 'whatsapp' in command:
        say('Opening Whatsapp')
        print('Opening Whatsapp...')
        webbrowser.open('https://web.whatsapp.com')
    elif 'bored' in command:
        say('Sorry, I cannot help you with that')
    elif 'nationality' in command:
        print('Your borders are merely a construct. I prefer to think myself as a citizen of the world')
        say('Your borders are merely a construct. I prefer to think myself as a citizen of the world')
    elif 'creator' in command:
        print('I was created by Manas')
        say('I was created by Manas')
    else:
        say('Sorry, I don\'t know that')