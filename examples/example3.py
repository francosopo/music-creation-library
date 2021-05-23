import pathlib
from crafters.regression import Regression
from crafters.scale import TraditionalScale
from crafters.instrument import AbstractInstrument
from crafters.melody import Melody

import math, os

scale = TraditionalScale(12)
melody = Melody(scale)
for i in range(12):
    melody.use_note(i,2) #(note index , duration)

class Instrument3(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody,**kwargs)
        self.regression = Regression(degree=8)
        self.regression.set_csv_directory(os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "timbres_data"))
        self.regression.load_csv("second_timbre")
        self.regression.generate()
    
    def timbre(self, note, armonic_number, time):
        return self.regression.use(2 * math.pi * note * armonic_number * time)

k = Instrument3(melody)
root_directory = pathlib.Path(__file__).parent.parent.absolute() # set the root directory as you want

render_directory = os.path.join(root_directory, 'creations')

k.set_render_directory(render_directory)
k.build_melody("melodia3")