import random as rnd
import numpy as np 
import pathlib, os, csv

from math import floor, pi, trunc
from time import time
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return trunc(number)

    factor = 10.0 ** decimals
    return trunc(number * factor) / factor
    

class Regression(object):
    
    def __init__(self,degree=4, period = 2*pi):
        super().__init__()
        self.X_points = []
        self.Y_points = []
        self.degree = degree
        self.period = period

    def __generate_random(self, seed, num_max_points):
        rnd.seed(seed)
        self.num_max_points = num_max_points
        for i in range(num_max_points):
            self.X_points.append(self.period*i/float(num_max_points))
            self.Y_points.append(rnd.random())
        self.X_points = np.array(self.X_points)
        self.Y_points = np.array(self.Y_points)
    
    def save_csv(self, name):
        if not os.path.exists(os.path.join(self.csv_dir)):
            os.mkdir(os.path.join(self.csv_dir))
        filename = os.path.join(self.csv_dir, f"{name}.csv")
        f = open(filename, "w")
        for i in range(len(self.X_points)):
            f.write(f"{self.X_points[i]}, {self.Y_points[i]}\n")
        f.close()

    def load_csv(self, name, column_names=False):
        with open(os.path.join(self.csv_dir, f"{name}.csv"), 'r') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=',')
            if column_names:
                line_count=0
            else:
                line_count=1
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.X_points.append(float(row[0]))
                    self.Y_points.append(float(row[1]))
        self.X_points = np.array(self.X_points)
        self.Y_points = np.array(self.Y_points)

        """dir = os.path.join(self.csv_dir,name)
        f = open(f"{dir}.csv", "r",encoding="utf-8")
        line = f.readline()
        while line != "":
            line = line.replace("\\n","")
            data = line.split(",")
            print(data)
            self.X_points.append(data[0])
            self.Y_points.append(data[1])
            line = f.readline()
        self.X_points = np.array(self.X_points)
        self.Y_points = np.array(self.Y_points)"""

    def __generate_regression(self):
        self.pipeline = make_pipeline(PolynomialFeatures(self.degree), LinearRegression())
        self.pipeline.fit(self.X_points.reshape(-1,1), self.Y_points.reshape(-1,1))
        
    def use(self, x, trunc_decimal=2):
        return truncate(self.pipeline.predict(np.array([[x-floor(x)]]))[0][0], trunc_decimal)

    def generate_randomly(self, seed=time(), num_max_points = 8):
        self.__generate_random(seed,num_max_points)
        self.__generate_regression()
    
    def generate(self):
        self.__generate_regression()

    def set_csv_directory(self, dir):
        self.csv_dir = dir