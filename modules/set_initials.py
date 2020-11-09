import os

def set_initials():

 #set values for training specifications
 batch_size = 32
 num_classes = 10
 epochs = 1 #Defines the amount of epochs to be processed
 data_augmentation = True
 num_predictions = 20
 
 #set model name and working directory
 model_name = 'keras_cifar10_trained_model.h5'
 save_dir = os.path.join(os.getcwd(), 'saved_models')
 return batch_size, num_classes, epochs, data_augmentation, num_predictions, model_name, save_dir
 
