import unittest
from KeyFinder import *


class TestFunction(unittest.TestCase):

    # defines audio path to test
    audio_path = 'une-barque-sur-l\'ocean.mp3'

    # generates a tuple consisting of an audio object y and its sampling rate sr
    y, sr = librosa.load(audio_path)

    # this function filters out the harmonic part of the sound file from the percussive part, allowing
    # for more accurate harmonic analysis
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    # this block instantiates the Tonal_Fragment class with the first 22 seconds of the above harmonic part of song
    unebarque_fsharp_min = Tonal_Fragment(y_harmonic, sr, tend=22)

    def test_chroma(self):
        unebarque_fsharp_min = Tonal_Fragment(TestFunction.y_harmonic, TestFunction.sr, tend=22)
        unebarque_fsharp_min.print_chroma()
        print("Test Completed")
        return True

    def test_key(self):
        unebarque_fsharp_min = Tonal_Fragment(TestFunction.y_harmonic, TestFunction.sr, tend=22)
        unebarque_fsharp_min.print_key()
        print("Test Completed")
        return True

    def test_corr(self):
        unebarque_fsharp_min = Tonal_Fragment(TestFunction.y_harmonic, TestFunction.sr, tend=22)
        unebarque_fsharp_min.corr_table()
        print("Test Completed")
        return True

    def test_chroma_img(self):
        unebarque_fsharp_min = Tonal_Fragment(TestFunction.y_harmonic, TestFunction.sr, tend=22)
        unebarque_fsharp_min.chromagram()
        print("Test Completed")
        return True


if __name__ == '__main__':
    unittest.main()
