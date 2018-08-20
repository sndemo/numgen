import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

def seq(size):
    return [ i for i in range (size)]

def create_dataset(dataset, look_back=5):
   dataX, dataY = [], []
   for i in range(len(dataset)-look_back-1):
      x = dataset[i:(i+look_back)]
      y = dataset[(i+look_back)]
      dataX.append(x)
      dataY.append(y)
   return np.array(dataX), np.array(dataY)


look_back = 5
trainX, trainY = create_dataset(seq(100), look_back)

# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
trainY = np.reshape(trainY, (trainY.shape[0], 1))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(look_back,1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=1000, batch_size=1, verbose=2)

# serialize model to JSON
json_model = model.to_json()
with open("numgen_model.json", "w") as json_file:
    json_file.write(json_model)

# serialize weights to HDF5
model.save_weights("numgen_model.h5")
print("Model saved to disk.")

# make predictions
print('Prediction for next number of 20,21,22,23,24', model.predict(np.array([[[20],[21],[22],[23],[24]]])))