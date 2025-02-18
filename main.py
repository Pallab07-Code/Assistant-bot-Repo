import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing shadow")
    #Listen when someone called jarvis

    while True:

        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2)
        
            print("processing your words:")
            command = r.recognize_google(audio)
            print(command)

            #for terminating shadow
            if(command == "ok bye"):
                speak("Good Day Sir ")
                break
        except Exception as e:
            print(f"Error {e}")
