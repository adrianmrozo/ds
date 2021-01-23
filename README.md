
# A Demonstration of Data Science Toolkits and Architectures - Image Recognition with Keras & Tensorflow on the CIFAR-10 dataset
by Ludwig Kraft & Adrian Mrozowski

## Description: 

**This repository demonstrates the capabilities of machine learning for image recognition and classification**

This repository is based on code from [Keras Team](https://github.com/keras-team), which demonstrates machine learning functionalities based on the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset.
It contains 60'000 small coloured 32x32 images subdivided into 10 different categories.
Those categories are airplane, automobile, bird, cat, deer, dog, frog, horse, ship & truck.
The first 50'000 images is considered as training data, which is used to train a Convolutional Neural Network (CNN).
The other 10'000 images can be used to test the performance of the model.

Without setting up anything on your machine, check out the code in our [Jupyter Notebook on Google Colab](https://colab.research.google.com/drive/1z95gJROm3aU2PaN4z1jZooFMTTbeSMz-?usp=sharing). It demonstrates the dataset and also the code that trains the model.

The CNN performs better, the more training rounds - "epochs" - are executed in the training process.
It achieves 75% validation accuracy in 25 epochs, and 79% after 50 epochs.
However, here the number of epochs equals one for the user to have a first demonstration of the results within an acceptable period of time, as one epoch as training even a single epoch can take up to 10 minutes. The accuracy after a single epoch is about 42%.

If a better performance of the model is desired the number of epochs can be increased accordingly in the *set_initials* module.


## Installation

### No or little experience with Docker and/or Python:

We tried to make it as simple as possible for the end user. If there is no prior experience with Docker, we strongly recommend using the [Docker Playground](https://labs.play-with-docker.com/).

After registration (free and straight forward) the user creates a new instance and can enters the following commands:

```
git clone https://github.com/adrianmrozo/ds
cd ds
docker-compose up
```

The 3 above commands do the following: 
1. Clones/copies this GitHub repository into a Docker Container on the website "play with docker"
2.  Enters the folder "ds"
3. Starts the prepared docker instructions, makes the code run

Then the CNN is trained and after completion (up to 10 minutes) the user can access a flask provided in port website to the prediction.
Click on the port numbers on the right side next to "Open Port".

In case the browser returns an error - "This page isn’t working" - just refresh/reopen the window.
The user gets to the welcome page.



### If Docker is already installed

Open the "ds" folder  in your terminal and enter the command:
```
docker-compose up
```
And everything should run by itself.

### For Ninja Pythoneers [not recommended]

You can install the required packages of the requirements file manually in the respective versions and run the *app* module in python from the "src" folder. However, this is not recommended, as this project was not optimized towards this usage. There are many dependencies within the packages. Docker is the most efficient way to use this code.


## Additional functionalities

This code is also starting a PostgreSQL database, and saves results out of the testing into the database.


## Additional information

This repository is the end product from several milestones, containing again several sub tasks. 
We documented our try and error and error process for each milestone in the *reports* folder. The accompanying code snippets for completing the sub tasks are stored in the folder "/src/legacy".


## Technical description

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

## Credits: 
Special Credits to supervisors [Sandro](https://github.com/sandroci) & [Arthur](https://github.com/habichta)

## License:
The original code in cifar10_cnn.py is part of Keras, please find its licence [here](https://github.com/keras-team/keras/blob/master/LICENSE).
