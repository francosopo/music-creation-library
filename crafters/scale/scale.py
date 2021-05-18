import math
import abc


class AbstractScale(object):

    def __init__(self, scale_length):
        self.scale = [0]*scale_length
        self.scale_length = scale_length
    
    """
    Define the scale with a function that sets the
    first armonic frequency of each one of the n notes
    """
    @abc.abstractmethod
    def define_scale(self, i, n):
        pass

    def make_scale(self):
        for i in range(self.scale_length):
            self.scale[i] = self.define_scale(i, self.scale_length)
    
    def get_tone(self, i):
        return self.scale[i]

class TraditionalScale(AbstractScale):

    def __init__(self, scale_length):
        super().__init__(scale_length)
    
    def define_scale(self,i,n):
        return 440*2**(i/12)





