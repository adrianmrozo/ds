from __future__ import print_function
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os


from setInitials import setInitials
batch_size, num_classes, epochs, data_augmentation, num_predictions, model_name, save_dir = setInitials() 
print(model_name)

from prep_cifar10 import prepareData
x_train, y_train, x_test, y_test = prepareData()

from test import testing
testing(model_name, save_dir, batch_size, y_test)

