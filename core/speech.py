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

    # Create unique temporary mp3
    temp_file = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    )

    filename = temp_file.name

    temp_file.close()

    try:

        asyncio.run(
            _generate_speech(
                text,
                filename
            )
        )

        pygame.mixer.music.load(
            filename
        )

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():

            time.sleep(0.1)

    finally:

        try:

            pygame.mixer.music.unload()

        except:

            pass

        try:

            os.remove(filename)

        except:

            pass