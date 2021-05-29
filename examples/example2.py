from crafters.scale import TraditionalScale
from crafters.melody import Melody

from examples.example1 import render_directory
from tests.instruments import InstrumentPolynomialRegression1

scale = TraditionalScale(12)
melody = Melody(scale)

j = InstrumentPolynomialRegression1(melody, quarter_note_duration=250)
j.set_render_directory(render_directory) #same render directory as example 1
j.build_melody("melodia2")