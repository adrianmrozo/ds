# Source: https://gurus.pyimagesearch.com/lesson-sample-running-a-pre-trained-network/#. Import the necessary packages
#from __future__ import print_function
from keras.models import load_model
from keras.datasets import cifar10
import numpy as np
import os
import matplotlib.pyplot as plt
from random import randint
 
def testing(model_name, save_dir, batch_size, y_test):

 # initialize the ground-truth labels for the CIFAR-10 dataset
 gtLabels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse",
	"ship", "truck"]
 
 # load the network
 print("[INFO] loading network architecture and weights...")
 model_path = os.path.join(save_dir, model_name)
 model = load_model(model_path)
 
 # randomly select a few testing examples from the CIFAR-10 dataset and then
 # scale the data points into the range [0, 1]
 print("[INFO] sampling CIFAR-10...")
 (testData, testLabels) = cifar10.load_data()[1]
 testData = testData.astype("float") / 255.0
 np.random.seed(42)
 idxs = np.random.choice(testData.shape[0], size=(15,), replace=False)
 (testData, testLabels) = (testData[idxs], testLabels[idxs])
 testLabels = testLabels.flatten()

 # make predictions on the sample of testing data
 print("[INFO] predicting on testing data...")
 probs = model.predict(testData, batch_size=batch_size)
 predictions = probs.argmax(axis=1)
 
 # loop over each of the testing data points
 for (i, prediction) in enumerate(predictions):
	 print("[INFO] predicted: {}, actual: {}".format(gtLabels[prediction],
		gtLabels[testLabels[i]]))

		
def test_one(model):
 # initialize the ground-truth labels for the CIFAR-10 dataset
 gtLabels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
 
  # scale the data points into the range [0, 1]
 print("[INFO] sampling one image from CIFAR-10...")
 (testData, testLabels) = cifar10.load_data()[1]
 testData = testData.astype("float") / 255.0
 idxs = np.random.choice(testData.shape[0], size=(1,), replace=False)
 (testData, testLabels) = (testData[idxs], testLabels[idxs])
 testLabels = testLabels.flatten()

 # make predictions on the sample of testing data
 print("[INFO] predicting on testing data...")
 probs = model.predict(testData, batch_size=32)
 predictions = probs.argmax(axis=1)
 
 # loop over each of the testing data points
 for (i, prediction) in enumerate(predictions):
	 print("[INFO] predicted: {}, actual: {}".format(gtLabels[prediction], gtLabels[testLabels[i]]))
	
 for (i, prediction) in enumerate(predictions):
  pred_label=gtLabels[prediction]
  test_label=gtLabels[testLabels[i]] 
 
 plt.imshow(testData[0])
 plt.imsave('test.png', testData[0])
	 
 return testData, test_label, pred_label, idxs[0]

 
 




