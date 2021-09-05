import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hello sir good morning boss")
    elif hour>=12 and hour<18:
        speak("hello sir good afternon boss")
    else:
        speak("hello sir good night boos have a nice another dayp ")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("wait for few moment")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
        return query


if __name__ == "__main__":
    wishme() 
 
    while True:

        query=takecommand().lower()
        
        if "wikipedia" in query:
            speak('searching in wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
