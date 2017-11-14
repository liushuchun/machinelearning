import numpy as np
import pandas as pd


class NaiveBayesClassifier(object):

    def __init__(self):
        self.data = list()
        self.label = list()
        self.pLabel1 = 0
        self.p0Vec = list()
        self.p1Vec = list()

    def load_data_set(self, file_name):
        datas = pd.read_csv(file_name)
        self.data=