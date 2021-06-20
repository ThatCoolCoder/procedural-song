import pyaudio
import math
import time
from procedural_song import MusicalKey

SAMPLE_WIDTH = 2
NUM_CHANNELS = 2
SAMPLE_RATE = 44100

audio_notes = []

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    data = []
    return (data, pyaudio.paContinue)

# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(SAMPLE_WIDTH),
    channels=NUM_CHANNELS,
    rate=SAMPLE_RATE,
    output=True,
    stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

# close PyAudio (7)
p.terminate()