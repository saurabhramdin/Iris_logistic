import pickle
import numpy as np
import pandas as pd
import config

class SpeciesType():
    def __init__(self,sepal_length,sepal_width,petal_length,petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

    def predict_target(self):
        self.load_model()
        test_array = np.zeros(4)
        test_array[0] = self.sepal_length
        test_array[1] = self.sepal_width
        test_array[2] = self.petal_length
        test_array[3] = self.petal_width

        predict_species = self.model.predict([test_array])

        target_names = {0:'setosa', 1:'versicolor', 2:'virginica'}
        
        return target_names[int(predict_species)]