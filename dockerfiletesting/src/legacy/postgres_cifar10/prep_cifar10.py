import keras
from keras.datasets import cifar10

#Preparing the data
# The data, split between train and test sets

def prepare_data():
 (x_train, y_train), (x_test, y_test) = cifar10.load_data()
 print('x_train shape:', x_train.shape)
 print(x_train.shape[0], 'train samples')
 print(x_test.shape[0], 'test samples') 
 return x_train, y_train, x_test, y_test



# Convert test and training class vectors to categorical class matrices.

def data_to_categorical(y_train, y_test, num_classes):
 y_train = keras.utils.to_categorical(y_train, num_classes)
 y_test = keras.utils.to_categorical(y_test, num_classes)
 return y_train, y_test
 
