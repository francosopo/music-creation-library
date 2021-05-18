from regression import Regression
import math
from scale import TraditionalScale
from instrument import AbstractInstrument
from melody import Melody


# Start creating a scale class
# Then, create a melody class using the scale you created
# Create an instrument class and override timbre method
# and then, build the melody and play it with the player 


class Instrument(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)

    def timbre(self, note, armonic_number, time):
        return math.sin(2 * math.pi * note * armonic_number * time)


scale = TraditionalScale(12)
melody = Melody(scale)

#create the melody
for i in range(12):
    melody.use_note(i,2)

#i = Instrument(melody)
#i.build_melody("melodia2")

"""class Instrument2(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)
        self.regression = Regression(degree=6)
        self.regression.generate_randomly(num_max_points=10)
        self.regression.save_csv("first_timbre")

    def timbre(self, note, armonic_number,time):
        return self.regression.use(2 * math.pi * note * armonic_number * time)
"""
#j = Instrument2(melody, quarter_note_duration=250)
#j.build_melody("melodia3")

class Instrument3(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody,**kwargs)
        self.regression = Regression(degree=8)
        self.regression.load_csv("second_timbre")
        self.regression.generate()
    
    def timbre(self, note, armonic_number, time):
        return self.regression.use(2 * math.pi * note * armonic_number * time)

k = Instrument3(melody)
k.build_melody("melodia3")