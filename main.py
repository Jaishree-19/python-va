import pyttsx3 as tts
import speech_recognition as sr
import wikipedia as wiki
import beepy
import googlesearch  #get urls
import pywhatkit as pyw #search in google
import csv


tts_obj = tts.init(driverName='sapi5')
voices = tts_obj.getProperty('voices')
tts_obj.setProperty('voice', voices[1].id)


def speak(audio):
    tts_obj.say(audio)
    tts_obj.runAndWait()

def takecommand():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print("Listening..")
        speak("listening")
        #beepy.beep(sound="ping")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio, language="en")
        print (f"you requested for:  {command}")
    except:
        speak("Sorry I could not understand what you said. Speak again ")
        takecommand()
    return command

def search_wiki(data):
    speak("Searching wikipedia....")
    data = data.replace("in wikipedia", "")
    data= data.replace("search for","")
    results = wiki.summary(data, sentences=4)
    speak("According to wikipedia ")
    print(results)
    speak(results)

def search_google(data):
    data=data.replace("search for","")
    data=data.replace("in google","")
    speak(f"Searching Google for {data}")
    pyw.search(data)

def search_youtube(data):
    data = data.replace("search for", "")
    data = data.replace("in youtube", "")
    speak(f"Searching Youtube for {data}")
    pyw.playonyt(data)

def add_item_list(data):
    data=data.replace("add","")
    data=data.replace("to the list","")


def add_to(data):
    data = data.replace("add","")
    data=data.replace("to the list","")
    speak(f"Adding {data} to the list")
    with open("list_s.csv","a") as file: # append mode
        writer = csv.writer(file)
        writer.writerow([data])
        file.close()



def show_list():
    speak("The items in the list are: ")
    with open("list_s.csv","r") as file:
        reader= csv.reader(file)
        for item in reader:
            speak(item)
            print(item)


if __name__ == "__main__":
  speak("Greetings! How may I help you?")
  while True:
    command = takecommand().lower()

    if "wikipedia" in command:
        search_wiki(command)

    elif "google" in command:
        search_google(command)

    elif "youtube" in command:
        search_youtube(command)

    elif"list" in command:
        if "add" in command:
            add_to(command)
        elif "show" in command:
            show_list()

    elif "stop":
        exit()












