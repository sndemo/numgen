import tensorflow as tf
import numpy as np
from Numgen import Numgen

numgen = Numgen()

print('Prediction for next number of 20,21,22,23,24', numgen.predict(np.array([[[20],[21],[22],[23],[24]]]), None))
#from numgen import Numgen
