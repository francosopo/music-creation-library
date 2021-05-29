import pathlib

from crafters.scale import TraditionalScale
from crafters.melody import Melody

from tests.instruments import InstrumentPolynomialRegression2
import math, os

scale = TraditionalScale(12)
melody = Melody(scale)
for i in range(12):
    melody.use_note(i,2) #(note index , duration)

k = InstrumentPolynomialRegression2(melody)
root_directory = pathlib.Path(__file__).parent.parent.absolute() # set the root directory as you want

render_directory = os.path.join(root_directory, 'creations')

k.set_render_directory(render_directory)
k.build_melody("melodia3")