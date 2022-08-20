from crafters.scale import TraditionalScale
from crafters.instrument import AbstractInstrument
from crafters.melody import Melody

import pathlib, os, math

# Start creating a scale class and override the method 'define scale'
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
    melody.use_note(i,2) #(note index , duration)

i = Instrument(melody)
root_directory = pathlib.Path(__file__).parent.parent.absolute() #set the render directory as you want
render_directory = os.path.join(root_directory, "creations")

i.set_render_directory(render_directory)
i.build_melody("melodia1")
