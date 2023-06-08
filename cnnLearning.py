from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
import time
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import os
from glob import glob

all_csv_files = []
for path, subdir, files in os.walk('.\\Documents\\fooData\\'):
    for file in glob(os.path.join(path, '*.csv')):
        all_csv_files.append(file)

def one_hot(y):
    yOneHot = np.zeros([len(y),len(np.unique(y))])
    for idx in range(len(y)):
        yOneHot[idx, np.where(np.unique(y)==y[idx])[0][0]] = 1
    return yOneHot

def evaluate_model(trainX, trainY, testX, testY):
    verbose, epochs, batch_size = 2, 10, 32
    n_timesteps, n_channels, n_outputs = trainX.shape[1], trainX.shape[2], trainY.shape[1]
    model = Sequential()
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps,n_channels)))
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    model.fit(trainX, trainY, epochs=epochs, batch_size=batch_size, verbose=verbose)
    _, accuracy = model.evaluate(testX, testY, batch_size=batch_size, verbose=verbose)
    return model, accuracy

X = []
yVal = []

for file in all_csv_files:
    df = pd.read_csv(file)
    data = np.dstack([df['amplitude'],df['rf']]).T
    X.append(data[:,:,0].T)
    yVal.append(file.split('cat_')[1][0])

y = one_hot(yVal)
X = np.array(X)
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.2, random_state=42)

model, accuracy = evaluate_model(trainX, trainY, testX, testY)

pred = model.predict(testX)
predY = [float(np.unique(yVal)[np.argmax(idx)]) for idx in pred]
testYVals = [float(np.unique(yVal)[np.argmax(idx)]) for idx in testY]
conf = confusion_matrix(testYVals, predY)

sns.heatmap(conf, annot=True)
