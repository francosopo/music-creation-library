import unittest as testing

from tests.instruments import *
from tests.abstract_tests import TestAbstractInstrument


class TestRegression1(TestAbstractInstrument):
    def setup(self):
        super().setUp()
        super().set_instrument(InstrumentPolynomialRegression1(self.melody))
        self.set_melody_name("melody2")

    def test_regression(self):
        self.setup()
        super().build()
        self.assertTrue(f"{self.melody_name}.wav" in self.rendered_melodies)


class TestRegression2(TestAbstractInstrument):

    def setup(self):
        super().setUp()
        super().set_instrument(InstrumentPolynomialRegression2(self.melody))
        super().set_melody_name("melodia3")

    def test_regression(self):
        self.setup()
        super().build()
        self.assertTrue(f"{self.melody_name}.wav" in self.rendered_melodies)


class TestBezierCurve(TestAbstractInstrument):
    def setup(self):
        super().setUp()
        super().set_instrument(InstrumentBezierCurve(self.melody))
        super().set_melody_name("melodia4")

    def test_regression(self):
        self.setup()
        super().build()
        self.assertTrue(f"{self.melody_name}.wav" in self.rendered_melodies)


if __name__ == "__main__":
    testing.main()
