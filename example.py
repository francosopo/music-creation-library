import math
from scale import TraditionalScale
from instrument import AbstractInstrument
from melody import Melody

# Start creating a scale class
# Then, create a melody class using the scale you created
# Create an instrument class and override timbre method
# and then, build the melody and play it with the player 


class Instrument(AbstractInstrument):

    def __init__(self, melody):
        super().__init__(melody)

    def timbre(self, note, armonic_number, time_frame):
        return math.sin(2 * math.pi * note * armonic_number * time_frame)

scale = TraditionalScale(12)
melody = Melody(scale)

#create the melody
for i in range(12):
    melody.use_note(i,2)

i = Instrument(melody)
i.build_melody("melodia2")