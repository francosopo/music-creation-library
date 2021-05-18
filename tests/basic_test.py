import pathlib

from crafters.scale import TraditionalScale
from crafters.instrument import AbstractInstrument
from crafters.melody import Melody

import math
import os
import unittest as testing


class Instrument(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)

    def timbre(self, note, armonic_number, time):
        return math.sin(2 * math.pi * note * armonic_number * time)

scale = TraditionalScale(12)
melody = Melody(scale)

#create the melody




class TestBasicTest(testing.TestCase):

    def setUp(self):
        self.scale = TraditionalScale(12)
        self.melody = Melody(scale)
    
    def test_basic_creation(self):
        for i in range(12):
            melody.use_note(i,2) #(note index , duration)
        
        root_directory = pathlib.Path(__file__).parent.parent.absolute()

        render_directory = os.path.join(root_directory,"creations")
        melody_title = "melodia2"
        i = Instrument(melody)
        i.set_render_directory(render_directory)
        i.build_melody(melody_title)

        dir = os.listdir(render_directory)
        self.assertTrue(f"{melody_title}.wav" in dir)
        
if __name__ == "__main__":
    testing.main()