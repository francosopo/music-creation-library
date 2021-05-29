import unittest as testing

from tests.instruments import *
from tests.abstract_tests import TestAbstractInstrument

class TestBezierCurve(TestAbstractInstrument):
    def setup(self):
        super().setUp()
        super().set_instrument(InstrumentBezierCurve(self.melody))
        super().set_melody_name("melodia4")

    def test_regression(self):
        self.setup()
        super().build()
        self.assertTrue(f"{self.melody_name}.wav" in self.rendered_melodies)

if __name__=="__main__":
    testing.main()