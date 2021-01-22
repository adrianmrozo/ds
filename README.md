# A Demonstration of Data Science Toolkits and Architectures - Image recognition with Keras & Tensorflow on the CIFAR-10 dataset
by Ludwig Kraft & Adrian Mrozowski

## Description: 

**This repository will demonstrate the capabilities of machine learning and image recognition**

This repository is based on a code from the Keras Team (https://github.com/keras-team) which demonstrates machine learning functionalities based on the CIFAR-10 dataset.
It is a dataset of 60000 32x32 colour images of 10 different categories.
The 10 categories are: airplane, automobile, bird, cat, deer, dog, frog, horse, ship & truck.
The code is first training a neural network with the 50000 pictures.
The other 10000 pictures can be used to see how well the model is performing.
You can find more background information about the dataset here:
https://www.cs.toronto.edu/~kriz/cifar.html

Please find also here our Google Colab file, that demonstrates the dataset and also the code that trains the model:
https://colab.research.google.com/drive/1z95gJROm3aU2PaN4z1jZooFMTTbeSMz-?usp=sharing

Please note that we have set the training epochs to 1, so that it is possible for the user to have within a good time period a first demonstration of the results.
And even to training 1 epoch can take up to 10 minutes, so if something does not display, it's well possible that the model is still training.
If you like to have a better model, you can take this code and change the number of epochs, the training time will increase accordingly.


## Installation:

**If you do not have any experience in Docker and/or Python:**

We tried to make it as simple as possible for the end user, if you never used Docker before, we strongly recommend to use the following site:

https://labs.play-with-docker.com/

You have to register (it's free and quite easy) and afterwards you can open a terminal.

You can enter the following commands:

```
git clone https://github.com/adrianmrozo/ds
cd ds
docker-compose up
```

The 3 above commands do the following 
1. You are cloning/copying this Github repository into the website "play with docker"
2. You are entering the folder "ds"
3. You are starting the prepared docker instructions by us, and our code will start to run

Next the model will train, and after the training is done (up to 10 minutes) you should be able to access the website with the prediction.
Click on the port numbers on the right side next to "Open Port".

If for some reason the browser will display:
"This page isn’t working", just refresh/reopen it again, so that you see "Welcome!"


**If you have Docker already installed:**

You can open in your terminal the "ds" folder, and enter the command:
```
docker-compose up
```
And everything should run by itself.

**If you have experience in Python [not recommended]:**

You can install the required packages out of requirements.txt file and try to run app.py in the "src" folder [not recommended, as not sufficiently tested and it was not optimized towards this usage, there too many dependencies regarding the packages.]


## Additional functionalities:

This code is also starting a PostgreSQL database, and saves results out of the testing into the database.


## Additional information:

This code is the end product from several milestones, containing again several sub tasks.
You can find the reports to each milestone in the "reports" folder and code completing the sub tasks in the folder "/src/legacy".


## Technical descriptions:


### Table of all packages including hashes

numpy == 1.18.5 \
    --hash=sha256:4674f7d27a6c1c52a4d1aa5f0881f1eff840d2206989bae6acb1c7668c02ebfb

imutils==0.5.3 \
    --hash=sha256:857af6169d90e4a0a814130b9b107f5d611150ce440107e1c1233521c6fb1e2b

keras==2.4.3 \
    --hash=sha256:05e2faf6885f7899482a7d18fc00ba9655fe2c9296a35ad96949a07a9c27d1bb

tensorflow==2.3.1 \
    --hash=sha256:87750a476aa6f76b3aad5e6182faf2a3036a3d4c0db3b6d7463ebbaf4b184a23

h5py==2.10.0 \
    --hash=sha256:d35f7a3a6cefec82bfdad2785e78359a0e6a5fbb3f605dd5623ce88082ccd681

psycopg2 == 2.8.6 \
    --hash=sha256:fb23f6c71107c37fd667cb4ea363ddeb936b348bbd6449278eb92c189699f543

matplotlib==3.3.3 \
    --hash=sha256:83e6c895d93fdf93eeff1a21ee96778ba65ef258e5d284160f7c628fee40c38f

flask==1.1.2 \
    --hash=sha256:8a4fdd8936eba2512e9c85df320a37e694c93945b33ef33c89946a340a238557

flask-ngrok==0.0.25 \
    --hash=sha256:724519a4dd3a2d374af50d4c0c21a26548737de0cf23f68dfb8d3b31c7311e93

random2==1.0.1 \
    --hash=sha256:34ad30aac341039872401595df9ab2c9dc36d0b7c077db1cea9ade430ed1c007

astunparse==1.6.3 \
    --hash=sha256:c2652417f2c8b5bb325c885ae329bdf3f86424075c4fd1a128674bc6fba4b8e8


### In- and Output

***Input:***
We feed the Neural Network with a dataset - the CIFAR-10 dataset, which is a large number of pictures grouped into non-overlapping classes. 
There exist training and test cases within the dataset.

***Output:*** 
- a trained Convolutional Neural Network

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
The  the code downloads data from https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz, which is the CIFAR-10 dataset discussed above.

## Credits: 
Special credits to Sandro & Arthur

## License:
cifar10_cnn.py is part of Keras, please find its licence [here](https://github.com/keras-team/keras/blob/master/LICENSE).
