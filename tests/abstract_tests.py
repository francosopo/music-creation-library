import unittest as testing
import os, pathlib

from crafters.scale import TraditionalScale
from crafters.melody import Melody

class TestAbstractInstrument(testing.TestCase):

    def setUp(self):
        self.scale = TraditionalScale(12)
        self.melody = Melody(self.scale)
        for i in range(12):
            self.melody.use_note(i,2)
        self.instrument = None
        self.render_directory = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'creations')

    def set_instrument(self, instrument):
        self.instrument = instrument
        self.instrument.set_render_directory(self.render_directory)
    
    def set_melody_name(self, name):
        self.melody_name = name

    def build(self):
        self.instrument.build_melody(self.melody_name)
        self.rendered_melodies = os.listdir(self.render_directory)
