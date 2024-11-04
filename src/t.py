import threading
from pydub import AudioSegment
from pydub.playback import play
import time


def play_sound(sound):
    play(sound)


time_played = 0.01

sound = AudioSegment.from_file("D:\\Shalaby Approved\\Frank Ocean - Nights.mp3")
sound_duration = round(((sound.duration_seconds / 60)), 2)

sound_thread = threading.Thread(target=play_sound, args=(sound,))
sound_thread.start()

while sound_thread.is_alive():
    print(f"{round(time_played, 2)} / {sound_duration}")
    time.sleep(1)
    time_played += 0.01
    if time_played == 0.60:
        time_played = 1

print("Sound has finished playing.")
