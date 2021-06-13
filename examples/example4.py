from examples.example1 import Instrument
from crafters.scale import TraditionalScale
from crafters.instrument import AbstractInstrument
from crafters.melody import Melody, MelodyCSVLoader

import pathlib, os, math

class Instrument(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)

    def timbre(self, note, armonic_number, time):
        return math.sin(2* math.pi * note*armonic_number * time)

scale = TraditionalScale(24)

#loading the melody from csv
root_directory = pathlib.Path(__file__).parent.parent.absolute()
csv_dir = os.path.join(root_directory,"melody_data")

melody = MelodyCSVLoader(scale,csv_dir)

csv_filename = "melody1.csv" 
render_directory = os.path.join(root_directory,"creations")
melody.load_csv(csv_filename)

instrument = Instrument(melody)

instrument.set_render_directory(render_directory)
instrument.build_melody("melodia5")
