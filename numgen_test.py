from numgen import Numgen
import numpy as np

numgen = Numgen()

print('Prediction for next number of 20,21,22,23,24', numgen.predict(np.array([[[20],[21],[22],[23],[24]]]), None))