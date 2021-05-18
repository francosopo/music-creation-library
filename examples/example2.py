from crafters.regression import Regression
from crafters.scale import TraditionalScale
from crafters.instrument import AbstractInstrument
from crafters.melody import Melody

from examples.example1 import render_directory

import pathlib, os, math

class Instrument2(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)
        self.regression = Regression(degree=6)
        self.regression.generate_randomly(num_max_points=10)
        self.regression.save_csv("first_timbre")

    def timbre(self, note, armonic_number,time):
        return self.regression.use(2 * math.pi * note * armonic_number * time)

scale = TraditionalScale(12)
melody = Melody(scale)

j = Instrument2(melody, quarter_note_duration=250)
j.set_render_directory(render_directory)
j.build_melody("melodia2")