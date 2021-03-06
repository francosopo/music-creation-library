import unittest as testing

from tests.instruments import InstrumentSineWave
from tests.abstract_tests import TestAbstractInstrument


class TestBasicTest(TestAbstractInstrument):

    def setup(self):
        super().setUp()
        super().set_instrument(InstrumentSineWave(self.melody))
        super().set_melody_name("melodia1")

    def test_instrument(self):
        self.setup()
        super().build()
        self.assertTrue(f"{self.melody_name}.wav" in self.rendered_melodies)
        
if __name__ == "__main__":
    testing.main()