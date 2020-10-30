from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os


def addModel(num_classes, x_train):
 model = Sequential()
 model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=x_train.shape[1:]))
 model.add(Activation('relu'))
 model.add(Conv2D(32, (3, 3)))
 model.add(Activation('relu'))
 model.add(MaxPooling2D(pool_size=(2, 2)))
 model.add(Dropout(0.25))

 model.add(Conv2D(64, (3, 3), padding='same'))
 model.add(Activation('relu'))
 model.add(Conv2D(64, (3, 3)))
 model.add(Activation('relu'))
 model.add(MaxPooling2D(pool_size=(2, 2)))
 model.add(Dropout(0.25))

 model.add(Flatten())
 model.add(Dense(512))
 model.add(Activation('relu'))
 model.add(Dropout(0.5))
 model.add(Dense(num_classes))
 model.add(Activation('softmax'))
 return model


#initiate RMSprop optimizer

def opt():
 opt = keras.optimizers.RMSprop(learning_rate=0.0001, decay=1e-6)
 return opt

