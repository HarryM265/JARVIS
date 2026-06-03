from modules.speech import speak
from modules.greeting import get_greeting
from modules.brain import ask_jarvis

print("JARVIS ONLINE")

speak(get_greeting())

while True:

    user_input = input(
        "You: "
    )

    if user_input.lower() == "exit":
        break

    response = ask_jarvis(
        user_input
    )

    speak(response)