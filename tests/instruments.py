from crafters.instrument import AbstractInstrument
from crafters.timbre_crafter import Regression, BezierCurve

import math, os, pathlib


class InstrumentSineWave(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)

    def timbre(self, note, armonic_number, time):
        return math.sin(2 * math.pi * note * armonic_number * time)


class InstrumentPolynomialRegression1(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)
        self.regression = Regression(degree=6)
        self.regression.set_csv_directory(os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "timbres_data"))
        self.regression.generate_randomly(num_max_points=10)
        self.regression.generate()
        self.regression.save_csv("first_timbre")

    def timbre(self, note, armonic_number,time):
        return self.regression.use(self.regression.period * note * armonic_number * time)


class InstrumentPolynomialRegression2(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody,**kwargs)
        self.regression = Regression(degree=8)
        self.regression.set_csv_directory(os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "timbres_data"))
        self.regression.load_csv("second_timbre")
        self.regression.generate()
    
    def timbre(self, note, armonic_number, time):
        return self.regression.use(self.regression.period * note * armonic_number * time)


class InstrumentBezierCurve(AbstractInstrument):
    def __init__(self, melody, **kwargs):
         super().__init__(melody, **kwargs)
         self.curve = BezierCurve()
         self.curve.set_csv_directory(os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "timbres_data"))
         self.curve.load_csv("second_timbre")
         self.curve.generate()
        
    def timbre(self, note,armonic_number, time):
        return self.curve.use(note * armonic_number * time)

