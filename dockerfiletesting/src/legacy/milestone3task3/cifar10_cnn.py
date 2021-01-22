'''
#Train a simple deep CNN on the CIFAR10 small images dataset.
It gets to 75% validation accuracy in 25 epochs, and 79% after 50 epochs.
(it's still underfitting at that point, though).
'''

from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os

batch_size = 32
num_classes = 10
epochs = 100
data_augmentation = True
num_predictions = 20
save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'keras_cifar10_trained_model.h5'

# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

trainimages=(x_train)
testimages=(x_test)
traincategorylabels=(y_train)
testcategorylabels=(y_test)

print(keras.backend.image_data_format())

(x_train, x_test) = cifar10.load_data()

allpictures =(x_train, x_test)

print(type(trainimages))
print(len(trainimages))
print(type(testimages))
print(len(testimages))
oneimage = testimages[1]
print(type(oneimage))
print(len(oneimage))
print(type(oneimage[1]))
notsurewhatthisis = oneimage[1]
print(type(notsurewhatthisis))
print(type(notsurewhatthisis[1]))
andnotsurewhatthisiscauseserrorifprinted = notsurewhatthisis[1]

print(type(traincategorylabels))
print(len(traincategorylabels))
print(type(traincategorylabels[1]))
print(len(traincategorylabels[1]))
print(traincategorylabels[1])
print(traincategorylabels[2])
print(traincategorylabels[3])
print(traincategorylabels[4])
print(traincategorylabels[5])
print(traincategorylabels[6])
print(traincategorylabels[7])
print(traincategorylabels[8])
print(traincategorylabels[9])
print(traincategorylabels[10])

print(type(oneimage))
print(len(oneimage))

print(testcategorylabels)
print(len(testcategorylabels))
print(type(testcategorylabels))
print(testcategorylabels[1])
