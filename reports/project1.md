
<![endif]-->

# Project Report

## Milestone 1

Group: Adrian Mrozowski & Ludwig Kraft

Date: 16 October 2020

Group: Adrian Mrozowski & Ludwig Kraft

Task 1
---------

### First Data Set Examination

We observe two datasets build by Alex Krizhevsky, Vinod Nair and Geoffrey Hinton consisting of millions of tiny colour images from the web.

#### <u> CIFAR </u>

1.) The CIFAR-10, which contains 60000 32x32 images sorted in 10 different classes. For each class there are 1000 randomly selected pictures from each class in the test batch. The rest of each class' images are in the training batch.

2.) The CIFAR-100 is a dataset like CIFAR-10, with the distinct fact of having 100 classes each containing 600 images with 500 training images and 100 testing images per class. The 100 classes are grouped into 20 super classes.

The classes are completely exclusive, which means there is no overlap of the classes. Each image is part of exactly one class. Both datasets are useful tools to train a multi-layer generative model that learns to extract meaningful features from images which resemble those found in the human visual cortex.

#### <u> What problem does it solve? </u>

The datasets help solving a classification problem of computer recognition. With the help of datasets as CIFAR, the deep learning approaches lead to major advances in computer vision to classify images, find objects in them, and label them with captions.

Task 2
---------

### First Encounter with ML Code

Skipping through the code and naively running it in the Python console made us aware of the missing **keras** package.

As it appears to be a package for deep learning applications within python, we checked [here](https://elitedatascience.com/keras-tutorial-deep-learning-in-python) to get the basics of the matter.

We discover the term of **Convolutional Neural Networks (CNNs)** and learn about their important property to efficiently handle high dimensions of raw data, which is the case with our datasets.

Code structure:

<u>We were surprised to find code of a machine learning project consisting of only 131 lines. </u> The structure of the code does not seem to be extremely complex.

It has some comments, which makes us understand the general idea what the code is doing.

Task 3
---------

### First Push to GitHub and Linux Command Line

We want to commit the code into our Git Repository.

First, copy pasted source code from GitHub to Spyder, saved it as cifar10_cnn.py in the local directory, which is also the local repository.

Then we created a new branch to set where to upload the files

```

$ git pull

```

to set our local repository is up to date

```

$ git checkout -b workon

```

to create the new branch "workon"

```

$ git push origin workon

```

to push the (empty / no changes) branch into git

Then we uploaded the file to GitHub with the following terminal commands:

```

$ git add cifar10_cnn.py

```

tracks respectively adds the file that we want to commit to the Git index (staging area). Use

```

$ git commit -m "First milestone: upload a first .py file to GitHub" cifar10_cnn.py

```

to commit & make a comment on the upload. And

```

$ git push origin workon

```

to push the newly tracked file into the GitHub branch 'workon'

Then <u>insert GitHub username and password</u> and the file is publicly available.

#### &rightarrow; successfully uploaded the file with comment

Task 4
---------

### Run the Python Code

#### Successful approach to run the code:

1. Copy & pasted the source code from GitHub into Spyder, saved it locally, and tried to run it

2. Received Error Message: ***ModuleNotFoundError:*** *No module named 'keras'*

3. Installed keras in Spyder with:

```
pip install keras
```

4. Received Error Message: ***ImportError:*** *Keras requires TensorFlow 2.2 or higher. Install TensorFlow via pip install TensorFlow*

5. Installed TensorFlow with:

```
pip install TensorFlow
```

6. Then it was possible to install keras as in 3.

7. Ran the script successfully

**Comment:** Please be aware that the code can run & train the model for hours. To test out if the code is running within a shorter time frame, you can change the epochs in line 18, from

``epochs = 100`` to ``epochs = 3``

#### Prerequisites and Dependencies:

Versions to run the code and python and dependencies, in ***bold*** what we consider relevant:

Hardware:

MacBook Air (13-inch, Early 2015)

Processor: 1.6 GHz Intel Core i5

8 GB 1600 MHz DDR3

Intel HD Graphics 6000 1536 MB

Software:

**OS Name: Ubuntu 20.04.1 LTS**

OS Type: 64-bit

GNOME: 3.36.3

**Anaconda Navigator 1.9.12**

**Spyder 4.1.4**

**Python: 3.8.3**

**Keras: 2.4.3**

**TensorFlow: 2.3.1**

With the following python command, we can check & add in the above list versions of further python packages:

```
pip list
```

**Note:** This a manual that tells stories about how we failed. Therefore, we also submit paths we went, but did not complete successfully or were necessary evils to start understanding the matter. Here is the first:

-----

#### Alternative and unsuccessful approach

***We tried a similar approach on a different machine:***

Different machine, system operating on Windows, but we also used anaconda navigator & Spyder, specifically anaconda prompt and the python environment in anaconda Spyder:

which led to nowhere.

It appears to be difficult to import the package keras as there are several other packages needed to install keras. We followed

http://xperimentallearning.blogspot.com/2019/08/python-install-keras-on-anaconda-in.html

to install the package via the command line.

We created a conda environment ``conda create --name deeplearning``, activated the environment (activate deeplearning) and installed keras

``conda install -c anaconda keras``. Since we are in a new environment, we need to reinstall certain packages: (conda install jupyter; conda install Spyder;

conda install matplotlib; conda install pandas) But still, it was not possible to import keras in Spyder.

Even though Anaconda prompt commands worked out properly and without errors, Spyder does not accept keras subsets, even though they should have been loaded with the provided code inside Spyder.

----

***Second approach, same machine & environment***

[Online](https://www.tutorialspoint.com/keras/keras_installation.htm) we learned that Keras is based on several other well-known packages. So, we went back to Anaconda prompt and installed NumPy, Pandas, Scikit-learn, Matplotlib, SciPy, Seaborn via shell command  ``pip install <package name>``. Then it was possible to install keras within Spyder. However, we could not import neither

keras sub packages like keras.datasets nor TensorFlow.

***New goal:*** Install keras subsets and TensorFlow in Python in Spyder IDE.

Tried manually installing keras.datasets and TensorFlow via ``pip install <package>`` within 'anaconda prompt'.

No result.

-----

***New try:*** anaconda prompt (which is similar to the Ubuntu command line, but in Windows)

```

python -c "import TensorFlow"

pip install TensorFlow

conda install Spyder

conda install theano

conda install TensorFlow

conda install keras

```

and I could also easily import theano, TensorFlow and keras in Spyder without error.

Still in Spyder after executing the code there would be an error that keras.datasets would not load.

```
pip install TensorFlow

pip install keras
```

both worked after downgrading python to version 3.7.0 with ``conda python==3.7.0``

and then installing TensorFlow and keras.

Still Spyder will not accept kera.datasets.

Updated Python again to 3.8. Somehow there are now ***kernel errors in Spyder***, which does not only sound terrible, but also could not be resolved. At this point this approach was given up, as eventually deleting & reinstalling some of the systems would be necessary.

----

**Out of the Box approach**

*On Windows*

***Deinstalled and re-installed Anaconda on Windows machine - then code ran successfully***

After initializing the Python environment in Spyder we used the following commands directly inside the console:

```
pip install — upgrade pip

pip install — upgrade setuptools
```

Only then we could easily install the necessary packages TensorFlow and keras. Mind the order.

```
pip install TensorFlow

pip install keras
```

Mind the fact that the first project code line

```
from __future__ import print_function
```

needs to be put into the literal first line of python.

Now the project code can easily run, which means the CNN is training itself with the provided dataset. It is running through 100 epochs and improving its accuracy in every epoch.

Snapshot: After only 19 epochs the CNN is reaching an accuracy of ~67.5%

**Outcome**

After some 6h of running the program in the Spyder environment it successfully terminated.

Furthermore, the output gave information on

Test loss: ~0.673

Test accuracy: ~0.780

----

**Out of the Box approach**

*On Ubuntu*

```
$ sudo apt update

$ sudo apt install git

$ git init

$ git pull <URL of git repository>

$ git config --global username "username"

$ git fetch

$ sudo apt update

$ pip3 install keras

$ pip3 install TensorFlow

$ python3 cifar10_cnn.py
```

Task 5
---------

### Explain the Code - What does it do?

#### 1.) In- and Output of the Neural Network

***Input:***

We feed the Neural Network with a dataset - in our case CIFAR-10 dataset, which is a large number of pictures grouped into non-overlapping classes.

There exist training and test cases within the dataset.

***Output:***

4 pieces of information:

- a trained CNN

- the location of the saved and trained Neural Network model

- test loss. A numeric value, which gives the mean of the squared error of classified cases

- test accuracy. A numeric value, which gives the number in % of correctly classified images of the test cases using the trained Neural Network.

#### 2.) What is Keras and how does it relate to TensorFlow?

Keras is a high-level Python neural networks library that runs on top of either TensorFlow or Theano and provides a Python interface for artificial neural networks.

Keras is a neural network library while TensorFlow is the open-source library for several various tasks in machine learning. Keras acts as an interface for the TensorFlow library.

#### 3.) How is the data loaded?

The data is being loaded with the following two lines of code:

```

from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

```

Then automatically the model downloads the dataset [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz), which was already discussed above in Task 1.

#### 4.) Which dependencies are imported?

TensorFlow: 2.3.1

Keras: 2.4.3

#### 5.) Type of neural network architecture:

CNNs (Convolutional Neural Network)

Task 6
---------

### README File for GitHub Repository

A documentation file was added to the root folder of our GitHub project. It explains step by step how to run the code. It is intended to be updated with each pull request to the master branch. It is formatted according the markdown syntax (see the Markdown Guide www.markdownguide.org). The documentation should be immediately visible in the web browser when accessing the GitHub project page. It was made in accordance with the GitHub Guide [Documenting your projects on GitHub](https://guides.github.com/features/wikis/).

***Most important element of the documentation are the steps on how to make the code run***

<u>Mandatory requirements:</u>

- **Python** (version 3.8.3 recommended)

- *Python packages (if not installed yet, see instructions below):*

- **Keras**: (version 2.4.3 recommended,

- **TensorFlow** (version 2.3.1 recommended)

######  Strongly recommended:

- OS: **Ubuntu** 20.04.1 LTS

- **Anaconda Navigator** 1.9.12

- **Spyder** 4.1.4

*Alternatively:*

- OS: **Windows 10**

- **Anaconda Navigator** 4.8.3

***Remark and reasons for our strongly recommended software***: *We have tested this code successfully in an Ubuntu environment with the Anaconda Navigator & Spyder Editor. In other environments first it was not possible for us to run the code. We therefore recommend strongly to also use this software, ideally even the same versions we used, see above. Alternatively, a new installation of Anaconda Navigator and Spyder for the Python environment is recommended.*

**If you are sure that you fulfil the above requirements, you can directly run the code.**

Otherwise make sure that you first install Ubuntu (Operating System), Anaconda Navigator (program), Spyder (program out of Anaconda Navigator), and see the below two steps to install the two remaining elements (two Python packages):

1. Install TensorFlow with the following command in your python console:

```

pip install TensorFlow

```

2. Install keras with the following command in your python console:

```

pip install keras

```

3. **You can now run the code.**

Please be aware that the code can run & train the model for hours. To test in less time, whether the code is running at all, you can reduce the epochs from 100 to 3 in line 18, from `` epochs = 100 `` to ``epochs = 3 ``

Task 7 & 8
---------

### GitHub Repository Setup

(task 7 was missing)

Create a folder for your report of this milestone in your GitHub project repository. Add the report and push it to GitHub.

1. Saved the markdown syntax as .md via one of the websites [stackedit.io](stackedit.io) or [dillinger.io](dillinger.io). **Remark:** Stackedit is also available as Desktop Version and very convenient to utilize.

2. Go to local directory and add the file ready to upload into git.

3. Checkout the branch you are in inside the repository with ``git branch`` and select the desired branch with ``git checkout <desired branch>`` and update the local folder with ``git pull``

4. Now make the file trackable via ``git add .`` or git add  < filename >

5. Comment your file with ``git commit -m "[your-commit-message]"``

6. Push the file into GitHub with ``git push``

7. Now check out your online repository. Your file will be available there.
