from pydub import AudioSegment
import numpy as np



class Audio:

    def __init__(self):
        sample_rate = 44100  # Sample rate in Hz
        duration = 10  # Duration of the song in seconds
        frequency = 440  # Frequency of the sine wave in Hz
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        audio_data = np.sin(2 * np.pi * frequency * t)
        audio_data = (audio_data * 32767).astype(np.int16)
        self.song = AudioSegment(audio_data.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)

    def save_audio(self):
        output_file = "new_song.wav"
        self.song.export(output_file, format="wav")
        print("New song created and saved as:", output_file)

    def append_song(self, file):
        new_sounds = AudioSegment(file)
        self.song.append(new_sounds, crossfade=1500)
