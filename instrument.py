import math
import abc
import wave
import struct

class AbstractInstrument(object):

    def __init__(self, melody):
        self.melody = melody.get_melody()
        self.scale = melody.get_scale()
        self.sample_rate = 44100
        self.black_duration = 500
        self.__compiled_melody = []

    @abc.abstractmethod
    def timbre(self, note, armonic_number, time_frame):
        pass

    def build_melody(self, name):
        for index_note,duration in self.melody:
            num_samples = duration * self.black_duration * self.sample_rate / 1000
            audio = []
            for j in range(int(num_samples)):
                sum = 1
                #superposition of 5 armonics
                for k in range(5):
                    sum += (1/5)*self.timbre(self.scale.get_tone(index_note),k,j/self.sample_rate)
                audio.append(sum)
            self.__compiled_melody += audio
        
        self.build_wav(name)
    
    def build_wav(self, name):
        wav_file = wave.open(f"{name}.wav", "w")
        n_channels = 1
        sampwidth = 2
        n_frames = len(self.__compiled_melody)
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((n_channels, sampwidth,self.sample_rate, n_frames, comptype, compname))
        for sample in self.__compiled_melody:
            wav_file.writeframes(struct.pack('h', int(sample * 16382)))
        wav_file.close()


class Player(object):
    @staticmethod
    def play(name):
        os.system(f"play {name}.wav")




    