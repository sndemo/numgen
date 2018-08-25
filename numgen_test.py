import numpy as np
import importlib

importlib.import_module("Numgen")
numgen = Numgen()

print('Prediction for next number of 20,21,22,23,24', numgen.predict(np.array([[[20],[21],[22],[23],[24]]]), None))
#from numgen import Numgen
