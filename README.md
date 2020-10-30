<<<<<<< HEAD
# Project name: DS group Ludwig & Adrian

## Description: 

**So far this repository contains the following code:**
https://github.com/keras-team/keras/blob/master/examples/cifar10_cnn.py

Please find it's dataset and more background information about it here:
https://www.cs.toronto.edu/~kriz/cifar.html


Please find a more detailled description after the installation guide.

## Installation guide: 
Please find below steps on how to make the code run. As it has some dependancies, the best way to make it run is to make sure to fulfill the requirements.
### Mandatory requirements:
- **Python** (version 3.8.3 recommended)
- *Python packages (if not installed yet, see instructions below):*
    - **Keras**: (version 2.4.3 recommended, 
    - **Tensorflow** (version 2.3.1 recommmended)
    - flask
	- redis
	- imutils
	- opencv-python

### Strongly recommended:
- OS: **Ubuntu** 20.04.1 LTS

*Alternatively:*
- OS: **Windows 10**
- **Anaconda Navigator** 4.8.3

***Remark and reasons for our strongly recommended software***: *We have tested this code successfully in an Ubuntu environment. In other environments first it was not possible for us to run the code. We therefore recommend strongly to also use this software, ideally even the same versions we used, see above.*	

**If you are sure that you fulfill the above requirements, you can try to directly run the code.**

Otherwise make sure that you first install Ubuntu (Operating System) and the below two two Python packages, the below is a summarized overview, the detailled step by step, command by command sintructions you will find further below:
1. Install tensorflow package
2. Install keras package
3. **You can now run the code.** *Please be aware that the code can run & train the model for hours. To test out if the code is running within a shorter time frame, you can reduce the epochs from 100 to 3 in line 18, from*
```sh
epochs = 100
```
to
```sh
epochs = 3
```

### Step by step, command by command instructions

Below a working step by step, Ubuntu terminal command by command instruction how to run the code successfully after downloading the **cifar10_cnn.py** file, the personal folder structure is just partly shown, generally the commands start after "$ ":

```sh
~$ sudo apt update
~$ sudo apt install git
~$ cd ds
~/ds$ git init
~/ds$ git pull https://github.com/adrianmrozo/ds.git
~/ds$ cd ..
~$ cd ..
/home$ cd ..
/$ cd ..
/$ pip3 install keras
/$ pip3 install tensorflow
```
*go back into your local repository again, with the "cd" command (use "ls" for orientation), until you're back were the file cifar10_cnn.py is located and type:*
```sh
~/ds$ python3 cifar10_cnn.py
```
*Et voilà! It should be running. In case you would like to reduce the processing time, you can reduce the amount of epochs as described above.*

## More detailled description

### In- and Output

***Input:***
We feed the Neural Network with a dataset - the CIFAR-10 dataset, which is a large number of pictures grouped into non-overlapping classes. 
There exist training and test cases within the dataset.

***Output:*** 
*4 pieces of information*
 - a trained CNN
- the location of the saved and trained Neural Network model
- test loss. A numeric value ,which gives the mean of the squared error of classified cases
- test accuracy. A numeric valie, which gives the number in % of correctly classified images of the test cases using the trained Neural Network.

### Dataset:
We observe two datasets build by Alex Krizhevsky, Vinod Nair and Geoffrey Hinton consisting of millions of tiny color images from the web.

1.) The CIFAR-10, which contains 60000 32x32 images sorted in 10 different classes. For each class there are 1000 randomly selected pictures from each class in the test batch. The rest of each class’ images are in the training batch.

2.) The CIFAR-100 is a dataset similar to CIFAR-10, with the distinct fact of having 100 classes each containing 600 images with 500 training images and 100 testing images per class. The 100 classes are grouped into 20 superclasses.

The classes are completely exclusive, which means there is no overlap of the classes. Each image is part of exactly one class. Both datasets are useful tools to train a multi-layer generative model that learns to extract meaningful features from images which resemble those found in the human visual cortex.

The datasets help solving a classification problem of computer recognition. With the help of datasets as the observed ones deep learning approaches lead to major advances in computer vision to classify images, find objects in them, and label them with captions.

##### What is Keras and how does it relate to Tensorflow? 
Keras is a high-level Python neural networks library that runs on top of either TensorFlow or Theano and provides a Python interface for artificial neural networks. 
Keras is a neural network library while TensorFlow is the open-source library for a number of various tasks in machine learning. Keras acts as an interface for the TensorFlow library.

##### How is the data loaded?
The data is being loaded with the following two lines of code:
```sh
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
```
Then automatically the model downloads data from https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz, which is the CIFAR-10 dataset discussed above.

##### Which dependencies are imported?
Tensorflow: 2.3.1
Keras: 2.4.3

##### Type of neural network architecture used: 
CNNs (Convolutional Neural Network)

## Credits: 
Special credits to Sandro & Arthur

## License: 
cifar10_cnn.py is part of Keras, please find its licence here:
https://github.com/keras-team/keras/blob/master/LICENSE
=======
# Project name: DS group Ludwig & Adrian

## Description: 

**So far this repository contains the following code:**
https://github.com/keras-team/keras/blob/master/examples/cifar10_cnn.py
Please find it's dataset and more background information about it here:
https://www.cs.toronto.edu/~kriz/cifar.html
Please find a more detailled description after the installation guide.

## Installation guide: 
Please find below steps on how to make the code run. As it has some dependancies, the best way to make it run is to make sure to fulfill the requirements.
### Mandatory requirements:
- **Python** (version 3.8.3 recommended)
- *Python packages (if not installed yet, see instructions below):*
    - **Keras**: (version 2.4.3 recommended, 
    - **Tensorflow** (version 2.3.1 recommmended)

### Strongly recommended:
- OS: **Ubuntu** 20.04.1 LTS

*Alternatively:*
- OS: **Windows 10**
- **Anaconda Navigator** 4.8.3

***Remark and reasons for our strongly recommended software***: *We have tested this code successfully in an Ubuntu environment. In other environments first it was not possible for us to run the code. We therefore recommend strongly to also use this software, ideally even the same versions we used, see above.*	

**If you are sure that you fulfill the above requirements, you can try to directly run the code.**

Otherwise make sure that you first install Ubuntu (Operating System) and the below two two Python packages, the below is a summarized overview, the detailled step by step, command by command sintructions you will find further below:
1. Install tensorflow package
2. Install keras package
3. **You can now run the code.** *Please be aware that the code can run & train the model for hours. To test out if the code is running within a shorter time frame, you can reduce the epochs from 100 to 3 in line 18, from*
```sh
epochs = 100
```
to
```sh
epochs = 3
```

### Step by step, command by command instructions

Below a working step by step, Ubuntu terminal command by command instruction how to run the code successfully after downloading the **cifar10_cnn.py** file, the personal folder structure is just partly shown, generally the commands start after "$ ":

```sh
~$ sudo apt update
~$ sudo apt install git
~$ cd ds
~/ds$ git init
~/ds$ git pull https://github.com/adrianmrozo/ds.git
~/ds$ cd ..
~$ cd ..
/home$ cd ..
/$ cd ..
/$ pip3 install keras
/$ pip3 install tensorflow
```
*go back into your local repository again, with the "cd" command (use "ls" for orientation), until you're back were the file cifar10_cnn.py is located and type:*
```sh
~/ds$ python3 cifar10_cnn.py
```
*Et voilà! It should be running. In case you would like to reduce the processing time, you can reduce the amount of epochs as described above.*

## More detailled description

### In- and Output

***Input:***
We feed the Neural Network with a dataset - the CIFAR-10 dataset, which is a large number of pictures grouped into non-overlapping classes. 
There exist training and test cases within the dataset.

***Output:*** 
*4 pieces of information*
 - a trained CNN
- the location of the saved and trained Neural Network model
- test loss. A numeric value ,which gives the mean of the squared error of classified cases
- test accuracy. A numeric valie, which gives the number in % of correctly classified images of the test cases using the trained Neural Network.

### Dataset:
We observe two datasets build by Alex Krizhevsky, Vinod Nair and Geoffrey Hinton consisting of millions of tiny color images from the web.

1.) The CIFAR-10, which contains 60000 32x32 images sorted in 10 different classes. For each class there are 1000 randomly selected pictures from each class in the test batch. The rest of each class’ images are in the training batch.

2.) The CIFAR-100 is a dataset similar to CIFAR-10, with the distinct fact of having 100 classes each containing 600 images with 500 training images and 100 testing images per class. The 100 classes are grouped into 20 superclasses.

The classes are completely exclusive, which means there is no overlap of the classes. Each image is part of exactly one class. Both datasets are useful tools to train a multi-layer generative model that learns to extract meaningful features from images which resemble those found in the human visual cortex.

The datasets help solving a classification problem of computer recognition. With the help of datasets as the observed ones deep learning approaches lead to major advances in computer vision to classify images, find objects in them, and label them with captions.

##### What is Keras and how does it relate to Tensorflow? 
Keras is a high-level Python neural networks library that runs on top of either TensorFlow or Theano and provides a Python interface for artificial neural networks. 
Keras is a neural network library while TensorFlow is the open-source library for a number of various tasks in machine learning. Keras acts as an interface for the TensorFlow library.

##### How is the data loaded?
The data is being loaded with the following two lines of code:
```sh
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
```
Then automatically the model downloads data from https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz, which is the CIFAR-10 dataset discussed above.

##### Which dependencies are imported?
Tensorflow: 2.3.1
Keras: 2.4.3

##### Type of neural network architecture used: 
CNNs (Convolutional Neural Network)

## Credits: 
Special credits to Sandro & Arthur

## License: 
cifar10_cnn.py is part of Keras, please find its licence here:
https://github.com/keras-team/keras/blob/master/LICENSE
>>>>>>> a07423b15a15dc0c0900b49bf721f67687047d91
