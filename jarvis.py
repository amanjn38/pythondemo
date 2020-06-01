import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell me how can I help you")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('amanjn002@gmail.com' , 'password')
    server.sendmail("amanjn002@gmail.com", to, content)
    server.close()


def takeCommand():
    # IT TAKES MICROPHONE INPUT FROM THE USER AND RETURNS STRING OUTPUT
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print("Please say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    # Logic for executing task based on a query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Aman\\Aman\\Aman Phone\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))

        elif 'the time' in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{startTime}")

        elif 'open android studio' in query:
            aspath = "C:\\Program Files\\Android\\Android Studio\\binstudio64.exe"
            os.startfile(aspath)

        elif 'email to aman' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "amanjn38@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry email not sent")

        elif 'quit' in query:
            exit()
            