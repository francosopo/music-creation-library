import csv, os, pathlib

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
        

class MelodyCSVLoader(Melody):

    def __init__(self, scale, csv_dir):
        super().__init__(scale)
        self.csv_dir = csv_dir

    def load_csv(self,name,column_names=False):
        with open(os.path.join(self.csv_dir,f'{name}'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            if column_names:
                line_count=0
            else:
                line_count = 1
            
            for row in csv_reader:
                if line_count ==0:
                    line_count += 1
                else:
                    self.use_note(int(row[0]), float(row[1]))
        
