######################
###########main module
######################


#import all necessary packages and functions
#from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

from imutils import paths
import numpy as np
import imutils
#import cv2
import os




#module 1
from set_initials import set_initials
batch_size, num_classes, epochs, data_augmentation, num_predictions, model_name, save_dir = set_initials() 


#module 2
from prep_cifar10 import prepare_data
x_train, y_train, x_test, y_test = prepare_data()


#module 2
from prep_cifar10 import data_to_categorical
y_train, y_test = data_to_categorical(y_train, y_test, num_classes)



#module 3
from shape_model import add_model
model = add_model(num_classes, x_train)



#module 3
from shape_model import opt
opt = opt()

#module 4
#Processing / Training
from training import train
x_train, x_test, model, opt = train(model, opt, x_train, x_test)


#module 4
from training import augment
x_train, y_train, x_test, y_test = augment(data_augmentation, x_train, y_train, batch_size, epochs, x_test, y_test, model)


#module 5
#OUTPUT:
# Save trained model
from output import save_cnn
model, model_path = save_cnn(model, save_dir, model_name)

from output import cnn_stats
model = cnn_stats(model, model_path, x_test, y_test)


#module 6
# load and test

from test import testing
testing(model_name, save_dir, batch_size, y_test)

return model
#####################################
#####################################






