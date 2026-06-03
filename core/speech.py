import asyncio
import edge_tts
import pygame
import tempfile
import time
import os

VOICE = "en-GB-RyanNeural"

pygame.mixer.init()


async def _generate_speech(text, filename):

    communicate = edge_tts.Communicate(
        str(text),
        voice=VOICE
    )

    await communicate.save(filename)


def speak(text):

    print(f"\nJARVIS: {text}\n")

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    )

    filename = temp_file.name

    temp_file.close()

    asyncio.run(
        _generate_speech(
            text,
            filename
        )
    )

    # Give Windows time to release the file
    time.sleep(0.25)

    pygame.mixer.music.load(
        filename
    )

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        time.sleep(0.1)

    pygame.mixer.music.unload()

    try:
        os.remove(filename)
    except:
        pass