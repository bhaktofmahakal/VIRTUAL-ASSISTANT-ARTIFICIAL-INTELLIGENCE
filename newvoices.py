import os
import pygame

def speak(text):
    voice = 'en-US-ChristopherNeural'
    data = f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
    os.system(data)

    # Check if the data.mp3 file was created successfully
    if not os.path.exists("data.mp3"):
        print("Error: data.mp3 file was not created.")
        return

    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("data.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Playback error: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
import os
import pygame

def speak(text):
    voice = 'en-US-ChristopherNeural'
    data = f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
    os.system(data)

    # Check if the data.mp3 file was created successfully
    if not os.path.exists("data.mp3"):
        print("Error: data.mp3 file was not created.")
        return

    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("data.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Playback error: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
