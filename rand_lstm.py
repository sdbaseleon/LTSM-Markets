# https://machinelearningmastery.com/learn-echo-random-integers-long-short-term-memory-recurrent-neural-networks/

from random import randint
from numpy import array
from numpy import argmax
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from csv import reader
import numpy as np
 
# generate a sequence of random numbers in [0, 99]
#def generate_sequence(length=25):
#	return [randint(-99, 99) for _ in range(length)]


lineNum = 0
closeInt = []
def generate_sequence():
	with open('F:\\Trading Journal\\data\\SP00H.txt', 'r') as read_obj:
   # pass the file object to reader() to get the reader object
		csv_reader = reader(read_obj)
	    # Iterate over each row in the csv using reader object
		anchor = 0
		lineNum = 0
		for row in csv_reader:
			if lineNum % 25 == 0:
				anchor = row[4]
			currClose = row[4]
			if anchor > currClose:
				closeInt.append(1000-int(float(anchor) - float(currClose)))
			else:
				closeInt.append(1000+int(float(currClose) - float(anchor)))
			lineNum += 1
	return closeInt
"""
def iterInt():
	for i in range(len(closeInt)):
		print(closeInt[i])
"""
# one hot encode sequence
def one_hot_encode(sequence, n_unique=100):
	encoding = list()
	for value in sequence:
		vector = [0 for _ in range(2000)]
		vector[value] = 1
		encoding.append(vector)
	return array(encoding)
 
# decode a one hot encoded string
def one_hot_decode(encoded_seq):
	return [argmax(vector) for vector in encoded_seq]
 
# generate data for the lstm
def generate_data():
	# generate sequence
	sequence = generate_sequence()
	# one hot encode
	encoded = one_hot_encode(sequence)
	# convert to 3d for input
	X = encoded.reshape(encoded.shape[0], 1, encoded.shape[1])
	return X, encoded

"""
generate_sequence()
iterInt()
# define model
"""
model = Sequential()
model.add(LSTM(15, input_shape=(1, 500)))
model.add(Dense(500, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
for i in range(25):
	X, y = generate_data()
	model.fit(X, y, epochs=1, batch_size=1, verbose=2)
# evaluate model on new data
X, y = generate_data()
yhat = model.predict(X)
print('Expected:  %s' % one_hot_decode(y))
print('Predicted: %s' % one_hot_decode(yhat))
