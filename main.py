import pyttsx3 as tts
import speech_recognition as sr
import wikipedia as wiki
import beepy

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
        beepy.beep(sound="ping")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        print (f"you requested for:  {command}")
    except:
        speak("Sorry I could not understand what you said. Speak again ")
        takecommand()
    return command

if __name__ == "__main__":
    speak("Greetings ! What do you want to search for")
    command = takecommand()
    speak("Searching wikipedia....")
    results= wiki.summary(command,sentences=4)
    speak("According to wikipedia ")
    print(results)
    speak(results)

