import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

# Hazel (British)
engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 155)

def speak(text):

    print(f"\nJARVIS: {text}\n")

    engine.say(text)
    engine.runAndWait()