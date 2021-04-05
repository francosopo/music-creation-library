from wave import open
from struct import pack

class Melody(object):
    
    def __init__(self,scale):
        self.__scale = scale
        self.__scale.make_scale()
        self.melody = []
    
    def get_scale(self):
        return self.__scale
    
    def use_note(self,index, duration):
        self.melody.append((index,duration))
    
    def get_melody(self):
        return self.melody
        