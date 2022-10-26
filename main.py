from KeyFinder import *
import librosa.effects

# defines audio path to test
audio_path = ''

# generates a tuple consisting of an audio object y and its sampling rate sr
y, sr = librosa.load(audio_path)

# this function filters out the harmonic part of the sound file from the percussive part, allowing
# for more accurate harmonic analysis
y_harmonic, y_percussive = librosa.effects.hpss(y)

# this block instantiates the Tonal_Fragment class with the first 22 seconds of the above harmonic part of une barque.
# the three methods called will print the determined key of the song, the correlation coefficients for all keys,
# and a chromagram, which shows the intensity of frequencies associated with each of the 12 pitch classes over time.
song_data = Tonal_Fragment(y_harmonic, sr, tend=22)
song_data.print_chroma()
song_data.print_key()
song_data.corr_table()
song_data.chromagram("Chromagram")

