import speech_recognition as sr
import pyttsx3
import webbrowser


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def CommandProcessing(word):
    if "open google" in word.lower():
        webbrowser.open_new_tab("https://www.google.com")
        speak("  opening google ")
    elif "open youtube" in word.lower():
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("  opening youtube ")
    elif "open facebook" in word.lower():
        webbrowser.open_new_tab("https://www.facebook.com")
        speak("  opening facebook ")
    elif "open instagram" in word.lower():
        webbrowser.open_new_tab("https://www.instagram.com")
        speak("  opening instagram ")
    elif "open maps" in word.lower():
        webbrowser.open_new_tab("https://www.google.com/maps")
        speak("  opening maps ")
    else:
        speak(" Sorry sir i did not understand your command")


if __name__ == "__main__":
    speak("Initializing shadow")
    #Listen when someone called shadow

    while True:

        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2)
        
            print("processing your words:")
            command = r.recognize_google(audio)
            print(command)

            #Wake up call
            if(command.lower() == "shadow"):
                speak("In your service sir")
                with sr.Microphone() as source:
                    print("Service mode activated")
                    audio2 = r.listen(source,timeout=2)
                    command2 = r.recognize_google(audio2)
                    print(command)

                    CommandProcessing(command2.lower())


            #for terminating shadow
            if(command == "ok bye"):
                speak("Good Day Sir ")
                break
        except Exception as e:
            print(f"Error {e}")
