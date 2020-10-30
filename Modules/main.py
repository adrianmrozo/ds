######################
###########main module
######################


#import all necessary packages and functions
from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os


#module 1
from setInitials import setInitials
setInitials() 

#module 2
from prep_cifar10 import prepareData
prepareData()

#module 2
from prep_cifar10 import dataToCategorical
dataToCategorical(y_train, y_test, num_classes)

#module 3
from shapeModel import addModel
addModel(num_classes, x_train)

#module 3
from shapeModel import opt
opt()

#module 4
#Processing / Training
from training import train
train(model, opt, x_train, x_test)

#module 4
from training import augment
augment(data_augmentation, x_train, y_train, batch_size, epochs, x_test, y_test)


#module 5
#OUTPUT:
# Save trained model
from output import saveCNN
saveCNN(model, save_dir, model_name, model_path)

from output import CNNstats
CNNstats(model, model_path, x_test, y_test)

#####################################
#####################################






