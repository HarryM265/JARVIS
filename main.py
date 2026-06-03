from core.speech import speak
from core.greeting import get_greeting
from core.logger import log_conversation
from core.router import route

print("JARVIS ONLINE")

speak(get_greeting())

while True:

    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        speak("Goodbye sir.")
        break

    response = route(user_input)

    speak(response)

    log_conversation(
        user_input,
        response
    )