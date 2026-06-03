import asyncio
import edge_tts
import os

async def speak(text):

    communicate = edge_tts.Communicate(
        text,
        voice="en-GB-RyanNeural"
    )

    await communicate.save("output.mp3")

    os.startfile("output.mp3")

asyncio.run(
    speak("Good evening sir.")
)