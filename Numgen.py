from keras.models import model_from_json
import numpy as np

class Numgen(object):
    def __init__(self):
        # load json and create model
        json_file = open('numgen_model.json', 'r')
        json_model = json_file.read()
        json_file.close()

        self.model = model_from_json(json_model)
        # load weights into new model
        self.model.load_weights("numgen_model.h5")
        self.model._make_predict_function()
        print("Numgen model loaded from disk.")

    def predict(self,X,features_names):
        return self.model.predict(X)
