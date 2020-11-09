# Save model and weights

from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os


def save_cnn(model, save_dir, model_name):
 if not os.path.isdir(save_dir):
     os.makedirs(save_dir)
 model_path = os.path.join(save_dir, model_name)
 model.save(model_path)
 return model, model_path


def cnn_stats(model, model_path, x_test, y_test):
 print('Saved trained model at %s ' % model_path)
 # Score trained model.
 scores = model.evaluate(x_test, y_test, verbose=1)
 print('Test loss:', scores[0])
 print('Test accuracy:', scores[1])
 return model
 
 
