# Project Report

## Milestone 2
Group: Adrian Mrozowski & Ludwig Kraft

Date:  October 30, 2020


Task 1
---------

### Clean git repositories are important


1.) **How to handle the existing branches - master**

We currently have 2 branches, that we treat as master file. The one called "main" is the default branch on github.
The other one called "master" contains the same information and needs to be set as default.
Repository Owner needs to follow the few simple steps in [here](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/changing-the-default-branch).


After we did that, we deleted the "main" branch.

2.) **How to handle the existing branches - workon**

Additionally there are two test branches. **testbranch** and **workon**.
We want to delete the **testbranch** and keep **workon** as a testbranch.


**Notes:**
Here I keep the most useful commands for handling pulls and pushes, creations and deletions of remote and local branches. This is a small insight into the inputs I've used to complete the task of editing the structure of the git repository.

<u> ***How to create a new branch and push it to github?*** </u>

```
$git branch <new_branch_name>
$git checkout <new_branch_name>
```

or both in just one line 

```
$ git checkout -b <new_branch_name> 
```

followed by

```
git push --set-upstream origin <new_branch_name>
```

<u> ***How to delete local branch?*** </u>

```
git branch -d <branch_name>
```

<u> ***How to delete remote branch?*** </u>

```
git push origin --delete remoteBranchName
```

<u> ***How to push file into certain remote branch?*** </u>

```
git push origin <remote_branch_name>
``` 

<u> ***How to pull default branch?*** </u>

```
git init
git pull <url_rep>
```


<u> ***How to pull just a single branch from github?*** </u>
 
```
git clone <url_rep> --branch <branchname>
```

**Notes: END** 


3.) **Specification of the .gitignore file**

All file types, respectively certain files within the local directory that are listed in the .gitignore file 
will be ignored when updating github to the status of the local directory. So we need to think about 
which files and filetypes we actually want to be displayed and shared on github. With our local directory 
growing (e.g. saving a trained CNN, adding text files with notes, ect.) and the premise to keep our repository 
nice and clean, we do not want all those newly added files to be uploaded into github.
Thus, with more and more files/file types to be stored locally and us not wanting those files to be shared, we have to 
update the .gitignore file on a regular basis.

In particular: 
- We ignore our and all saved and trained CNN. We use: *.h5
- As specifically asked for in the instructions of this project, we want to avoid all pictures, video and music.

We restrict some file types as representatives. We use: 
for music: *.mp3, *.wav, *.flac 
for videos: *.mp4, *.mov, *.wmv, *.avi
for pictures: *.jpg, *.png, *.tiff, *.gif, *.raw

We already created a .gitignore file for Milestone 1. We copied the text and created via ```git touch``` a new 
text file. We added some wildcards for additional file types. 

Just upload the .gitignore to the workon branch.

**Problem:** Somehow I uploaded the entire folder workon into the branch workon. 
**Solution:** When uploading the folder workon the wd wasn't set within workon, but one folder layer above. Thus the folder was uploaded entirely and not just the content of the local folder workon.


In general there was a certain level of confusion for a time as in the local repository only a master branch was found and the newly created workon branch couldn't be pushed into github. In the end there were many folders and branches and files calles "workon". This did not add towards a solid workflow.
***Learning:***

- mind your wd! Before pushing or pulling ensure that you are set in the correct location
- mind your folder and branch names

5.) ***Version control of the .gitignore - strategy***

**First idea:**
Use 4 branches within the repository: Master, workon_shared, user_1, user_2
Like this every team member can work on his own, separate branch. Additionally, files that need to be shared can be uploaded in the workon branch. Whenever files are being pushed into the master branch, a pull request 
needs to be confirmed by the other team member. 
Therefore we create the two new branches: workLK and workAM.

**Final and better idea:**
Use 2 branches within the repository: master, workon
Every team member working on the project, is updating his local data by pulling the workon branch before he starts working. He also updates the workon branch when he's done working. 
Like that the workon branch is always up-to-date. (including the .gitignore file)

Before releasing anything to the client side (towards the master branch) the workon branch is being pushed into the master branch. We do this via a pull request, which needs to be confirmed by the other team member.


6.) **Prohibit direct uploads to the master branch:**

The owner of the repository has to follow [these steps](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/enabling-required-status-checks).

However, now there are only unsupervised merges prohibited. 


7.) ***Problems encountered:*** 

  *Connecting the local directory to the online repository?*
  
In my understanding after cloning the repository to the directory there should all branches from the repository be also available locally. But when I checked via git branch, we encountered only a master branch. From there we cannot add files to a different branch as do not want to make a push towards the master branch of the repository.

**Solution:** Create a branch with a name like the branch you want to push files to.

*How to edit and upload a .gitignore file?* 

Whenever I create the .txt file and rename it respectively, it disappears. How can I load or push the file that doesn't get displayed?

***Solution:*** Checked the introduction video once more. Create the file not via a text editor but via ```touch .gitignore```. 

Make the file visible in the Ubuntu folder with 'ctrl+H'. 
Then the file can easily be edited and is also recognized by the ```git status``` command. 

Now the .gitignore file can be edited and then uploaded.


Task 2
----------

### This week's vocabulary

1.) ***What is a hash function? For what is it being used?*** 

A hash function is a mathematical function that converts an input value (key, object, numerical, etc.) into another compressed numerical value (integer), the so called hash value. The input to the hash function is of arbitrary length but output is always of fixed length.

The hash values are often used as address keys for data inside an array. Thus search time for values can be decreased significantly (from O(log n) to O(1)).

Equal inputs receive the same hash value, whereas each two inequal inputs never get the same hash value.

*Example:* 
Book call number. In a library each book has a unique call number. The call number works like an address of the book within the library. 
If the same book is displayed multiple times they have the same call number, but to different books never have the same call number. 
With the book number one can easily navigate through the library and find the book much faster than checking every single book until the desired one is found. 


2.) ***Difference between python modules, packages and scripts***

#### Scripts:
A python script is the code we can find in every python file, i.e. the entirety of all letters, words, numbers, variables, characters, functions, calculations, allocations, assignments, ect.
A script can be run directly in python, in Ipython or any python shell (e.g. Spyder or Google Colab).
A script saved as a python file is a module.


#### Modules:
Any python file is a module. Its name is the file's base name without the ".py" ending. Consider a function we might have implemented in python and we name the file  `test.py´ Then we call this module "test".

It is considered as a best practice to split large Python code blocks into modules containing up to 300–400 lines of code.
This best practice is called **"Modularization"**. 
It makes coding and development in python 
- *easier :* one only has to deal with a relatively small portion of the problem; coding is less error-prone
- *maintainable:* editing a single line in a large piece of code can cause errors due to interdependencies of the changed line. If a code is cut into modules that work separately it decreases the likelihood that impacts of towards other parts of the code occur.
- *reusable:* Functionality defined in a single module can be easily reused
- *scoping:* Modules typically define a separate namespace, which helps avoid collisions between identifiers in different areas of a program.

#### Packages:
A package is a collection of python modules or in more detail: This collection is structured as a dictionary with an additional _init_.py file. This _init_.py distinguishes a package from a directory.

When we import a package only the variables/functions/classes in the _init_.py file are visible. Sub-packages or modules are not. 
One needs to import those separately. (compare importing keras and keras.datasets of our project code in python)

The distinction between module and package works only on the file system level. When a package or module is imported into python, they are both treated equally as type _module_. 

Depending on a Python application, one can consider to group the modules in sub-packages such as doc, core, utils, data, examples, test.

_init_.py is executed once when a module inside the package is referenced. This file can be left empty, or package-level initialization code can be implemented optionally.



3.) ***Explain Docker container and Volume***

#### Docker container:
Docker is a platform that packages an application and all its dependencies together in the form of containers. This containerization aspect of Docker ensures that the application works in any environment. So to speak out of the box.

Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

On Docker each and every application runs on separate containers and has its own set of dependencies and libraries. This makes sure that each application is independent of other applications, giving developers reassurance that they can build applications that will not interfere with one another.

#### Docker volumes:
Docker volumes are file systems mounted on Docker containers to preserve data generated by the running container.

The volumes are stored on the host memory, independent of the container life cycle. This allows users to back up data and share file systems between containers easily.
For example, whenever we use an application via docker, that application created data (e.g. a CNN) and we want to save the data locally, we can use docker volumes to extract the data from the container. If the container is now deleted or reused, we prevent loss of data.


4.) ***Preference of using virtualenv vs. Docker. When would we use one or the other?*** 

We would use virtualenv when want to test something out on our local machines, prior to put it into operation, it is like our local workbench. However we can also use directly Docker, which is meant for the operational code.


5.) ***What is the Docker build context?***

"The docker build command builds Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified PATH or URL. The build process can refer to any of the files in the context. For example, your build can use a COPY instruction to reference a file in the context." [Source](https://docs.docker.com/engine/reference/commandline/build/).


6.) ***How can one assess the quality of a python package on PyPI?***

By checking how many stars it has for example. Funny example, by accident one of the team members installed the package "paths" instead of the package "imutils". A misunderstanding after looking at the code line: 
'''from imutils import paths'''

After installing "paths" a weird error message was shown. Comparing the two packages on PyPi:
imutils has 3348 stars (https://pypi.org/project/imutils/) while paths (https://pypi.org/project/paths/) has 0 stars. Said team member is slightly worried now. 



Task 3
--------- 

### Updating the code

In Milestone 1 we already accomplished the following tasks, respectively we know that the code has the following functionality:
- Can load data
- Can train (fit) a neural network on the data
- Can save a fitted model to a ".h5" file

Therefore we had to focus on the following two functionalities:
- Can load a ".h5" file, using Keras
- Can perform predictions using a "fitted" model, using Keras

Load a ".h5" file is very easy, we created a file (loadmodel.py) with this one python code line:

`model = load_model('keras_cifar10_trained_model.h5')`

However to perform predictions with the code, was significantly more challenging. 
Even though we found a command which should run the model on a given dataset, we had the feeling, that the dataset part is challenging in this case, as a larger part of the cifar10 code seems to prepare the dataset. [Here](https://gurus.pyimagesearch.com/lesson-sample-running-a-pre-trained-network/) we found a solution: 


We tried the provided code by creating a test_network.py file with their code and executing the following command in the terminal:

```
python3 test_network.py --model keras_cifar10_trained_model.h5 --test-images test_images
```

Unfortunately in a first try/run the following error message appeared:

```
File "test_network.py", line 5, in <module>
    from imutils import paths
ModuleNotFoundError: No module named 'imutils'
```

So we had to install the package imutils:

```
pip3 install imutils
```

After receiving another error message regarding a missing package, and after some research we also installed the opencv package:

```
pip3 install opencv-python
```

We tried to run the code again:

```
python3 test_network.py --model keras_cifar10_trained_model.h5 --test-images test_images
```

This time successfully, a bird picture popped up and the terminal said the following:

```
[INFO] sampling CIFAR-10...
[INFO] predicting on testing data...
[INFO] predicted: bird, actual: bird
[INFO] predicted: truck, actual: automobile
[INFO] predicted: frog, actual: dog
[INFO] predicted: ship, actual: ship
[INFO] predicted: horse, actual: truck
[INFO] predicted: cat, actual: cat
[INFO] predicted: ship, actual: ship
[INFO] predicted: truck, actual: truck
[INFO] predicted: airplane, actual: airplane
[INFO] predicted: truck, actual: automobile
[INFO] predicted: horse, actual: dog
[INFO] predicted: automobile, actual: automobile
[INFO] predicted: cat, actual: cat
[INFO] predicted: dog, actual: dog
[INFO] predicted: automobile, actual: truck
[INFO] testing on images NOT part of CIFAR-10
```

On our machine all the above pictures were shown. We would also like to highlight the model was trained on another machine, and run with this python file on the machine of the other team member successfully. 
The images not part of CIFAR-10 were not shown anymore, we think it might be because the website actually asks for 95$ monthly so that one can download the code, so maybe the displayed code on the website was not the entire code. 
For our purposes to try to run the fitted model on another machine for a first time (even if it is just on testing data as written above), it was sufficient, we managed to fulfill:

#### &rightarrow; Can perform predictions using Keras


Task 4
-----------

### Modularization of Python Code 

First we get to know the concept of modularization. 
The idea is to cut our project code in small sections that each one semantically independent. 

The whole code could be easily reassembled by linking the modules together again. However, we will have one 'main.py` file, where parts of the modules will be run in the respective order. 

**Goal:**
After the modularization the code should run just like it did before with the important difference that the code will be found cut into snippets stored in several modules which are again all called at least once in the 'main.py` file.


**Procedure:** 
As we already extensively commented the Code in the Milestone 1, it was easy to find lines on where to split the code into semantically depending sections. 
In a first attempt to modularize we found our Code to be divided into 5 modules with their functions (in brackets):
- setInitials (setInitials)
- prep_cifar10 (prepareData, dataToCategorical)
- shapeModel (addModel, opt)
- training (train, augment)
- output (saveCNN, CNNstats)

The role of functions within the modules are self-explanatory as their names are well-chosen and their sections in the original code were well-divided.

Most of those modules contain 2 functions, some only one. 
By rewriting all code into functions that then can be used in the 'main.py`  file, we noticed the utmost importance of checking all variables that are being used in a particular function and also to declare them as variables for the function. 

Otherwise the function would never know, which values should be used. 
one can run the code easily with the command ``python3 main.py``

Of course the modularization did not work initially. After trying to run the modularized code in python, there were several errors, some of them we want to discuss in a quick manner.  

1.) ***Set-up***
As described in Milestone 1 we always have to set up our python environment properly before we can even attempt to run the code. Errors suggested that packages keras and tensorflow were missing, which we could again easily install via 

```
pip3 install keras
pip3 install tensorflow
```

**Learned:** Whenever necessary: First, set up your python environment before running code.


2.) **Several small typing errors** 

Fix errors in the modules and error search: easy

After running the code for the first time there occured some typos, which caused error messages like that

```Traceback (most recent call last):
  File 'main.py`, line 27, in <module>
    dataToCategorical(y_train, y_test, num_classes)
NameError: name 'y_train' is not defined
```

So it is easy to find the respective module (here, we import *dataToCategorical* from *prep_cifar10*, thus we check *prep_cifar10* and look there at the function *dataToCategorical*. We noticed that the ":" were missing do well-define the function. 

or: 

```
File "main.py", line 59, in <module>
    saveCNN(model, save_dir, model_name, model_path)
NameError: name 'model_path' is not defined
```

I thought a model path was defined at the beginning in *setInitials*. Therefore I checked the function *setInitials()* and found that this wasn't the case. So I checked the the error function once more and noted that *model_path* was just defined within the respective function. We simply had to erase the variable from the function AND as argument in the respective function of the *'main.py`* file.

There occured several small and relatively easy-to-solve errors, which won't bring any more insight for the reader of this report. However, we had to deal with them anyway and solved them all for you, you're welcome.


3.) ***How to correctly put the variables into the main script?*** 

After the note that modules should only constist of definitions and imports I first thought, this might apply to the main.py file as well. 

It was pretty difficult to put the output variables of a function again as input in another function. 
The goal was that functions in the 'main.py` file could reuse variables that have been changed or updated by other functions, e.g. *x_train* is created with *prepareData()*, updated by *train()* and used again by *augment()*. 

I experimented with **naming variables** before the return statement, i.e. ```return y_test, y_train = (y_test, y_train)``` in multiple versions of setting brackets. 

All attempts failed to make the variable created in a function accessable in the main envidronment. 

As we wanted to avoid defining variables and allocating objects to them, I tried my luck with object selection:

e.g. in an earlier stage *prepareData()* gave the output ``(x_train, y_train), (x_test, y_test)`` when we needed the *x_train* object again I selected it via `` prepareData()[0][0] ``.

This enabled me to use the *x_train* object, but also ran the *perpareData()* function again. I re-implemented the Modularization completely new with this method. 

A module in the main file could then look like this:

```
from training import train
train(addModel(setInitials()[1], prepareData()[0][0]), opt(), prepareData()[0][0], prepareData()[1][0])
```

How stupid!

**The code ran**, but several functions were run multiple times. Python never finished, but the process was *killed* after some running time.

**Huge downside:** like this all print statements were printed in the console and more importantly this took computing power only for the sake of not using variable allocations. 
Additionally: The code appeared to be very complicated which such a large number of assignments and the style seemed to be far from clean PEP8 implementation. 

#### &rightarrow; This could not be the solution! 


4.) ***Final and successfull approach***

So I went further and re-thought the limits of definitions and imports. I noticed that defining variables only using functions was still a legitimate approach, which will solve my problem. So instead of only code like 
`addModel(num_classes, x_train)`
I also allowed code like 
`model = addModel(num_classes, x_train)`

In that way we can easily reuse the results of working functions and edit them in an ongoing basis.  

5.) ***Kills***

However, when I ran the main file in Python after some time the process kept on to be killed. I did not know, **why** the process was killed and neither knew I **were** exactly. 

For the second problem of the exact spot, where the code was killed, I used a well-known technique to figure out bugs. I added **print statements** inside after every module in the main file. Every short module-note that was printed, signaled me that the module could run without error. 
I located the training module and the train function as error term. I kept on searching with my exclusion method and ended up at the lines 

```
 x_train = x_train.astype('float32')
 x_test = x_test.astype('float32')
```

I investigated the objects and found that both *x_train* and *x_test* were ndarrays. The *astype()* function is a general function. However, dealing with arrays always screams that working with *numpy* is a good idea. So I tried reformulating the two lines (two examples out of many): 

``
x_train = numpy.float32(x_train)
``

or

``
x_train = numpy.x_train.astype('float32')
``

After too much time of try and error (and only errors) I decided that the problem won't be solved by changing the code.

When searching for reasons why a process was being killed in python, I found the command 

```
dmesg -e
```

which can be used to confirm whether Linux itself killed the process due to OOM (Out Of Memory, a lack of the systems's memory)
Lack of memory on my virtual machine appeared to be the problem why the code was always being killed.
Figuring out this fact cost me some 4h.
 
I had the idea of changing the number of epochs to run the code also with less memory. 

As we understand the code more and more it was easy to change the epoch number to 1 in the *setInitials* module for test purposes (epochs are now again back on 100)

The code ran perfectly with reduced epochs and therefore the first **modularization of the project code has been finished successfully.**

----

**Loading and Testing**
However, we did not yet check the new functionalities of the code that we added in Task 3.
Our code should not only be able to train and save a model, but also load and test it. 
Adrian, did a great job, when he managed to load and test a CNN in via the terminal! 

For this task, however, we also want to include those functionalities into the actual python code. Therefore, Ludwig had to slightly modify our the modularized project code.

**Goal:**
We want to shift the load and the test code in two modules, respectively two functions. As I found that loading the model was already a part of the test code, we aim for only one module named 'test.py`. 
As the complete project code trains the model, which composes of lots of computing power and we do not always want to train a new CNN whenever running the code, we want to come out with a second module called ´load_and_test.py' that can load a trained CNN and then test it. 

**Procedure:**
1.) **test_network to module test and function testing**

- Avoid parsing inputs: 

We delete all parsing lines.

```
 #construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="path to output model file")
ap.add_argument("-t", "--test-images", required=True,
	help="path to the directory of testing images")
ap.add_argument("-b", "--batch-size", type=int, default=32,
	help="size of mini-batches passed to network")
args = vars(ap.parse_args())

# initialize the ground-truth labels for the CIFAR-10 dataset
gtLabels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse",
	"ship", "truck"]
```
- load network

We substitute the line 

```
model = load_model(args["model"])
```

with 

```
model_path = os.path.join(save_dir, model_name)
 model = load_model(model_path)
```
After a CNN was trained by the project code it usually gets saved in the working directory and the new folder *saved_models*. With those two line from above we are able to access the trained modell in that particular folder.

- change batch size as input from arg function
```
 probs = model.predict(testData, batch_size=batch_size)
```
Before batch size was called via the code piece `args["batch_size"]` As we got rid of all arg functions, this had to be adopted as well. So I decided to use batch size as input for the function testing. The same applied for the line `probs = model.predict(kerasImage, batch_size)` later on in the script.

- test_images

We need to insert some test images within the line  
```
for imagePath in paths.list_images(args["test_images"]):
```
I decided that we can also use images, we already imported and therefore used y_test as input for the function. 
```
 for imagePath in paths.list_images(y_test):
 ```
- Updating Packages

 The code wouldn't run again and we quickly noticed that there were some new packages that we also have to include before the code runs smoothly. 
```
import numpy as np
import imutils
import cv2
import os
```
Now we are done editing the function testing and the module test.

It remains building it firstly into the main file and secondly the load_and_test file.

2.) **Function testing into main and load_and_test**
To ad the test function to **main** is easy as all variables(model_name, save_dir, batch_size, y_test) are already available in the main environment. We simply import the function testing via the module test into main: 

```
from test import testing
testing(model_name, save_dir, batch_size, y_test)
```

Secondly, we want to **load and test** a CNN without running the complete CNN training procedure. 

As we still need certain variables as input for testing, we could not just run testing without any set-up. 
We somehow need values for the variables 
model_name, save_dir, batch_size and y_test.

We want to load a model that is stored in save_dir, with the name model_name, a batch_size and test images y_test.
 We get these variables with the following commands and function calls:

```
from setInitials import setInitials
batch_size, num_classes, epochs, data_augmentation, num_predictions, model_name, save_dir = setInitials() 
print(model_name)

from prep_cifar10 import prepareData
x_train, y_train, x_test, y_test = prepareData()
```

Now we are set to run testing:

```
from test import testing
testing(model_name, save_dir, batch_size, y_test)
```

Whenever we run the load_and_test file with ``python3 load_and_test.py`` the CNN loads and then classifies a picture as "bird", which is then confirmed to be a bird. 
Finally, a 32x32 picture of a bird is displayed. However, we have to end the process manually.
Still - a success!


**Problems encountered:**
- IntendationErrors
As correct intendations are difficult to repair in the editor, I chose to use Spyder for the task as we have a more automated intendation there and even get the lines displayed, where errors occur. 
- Kills
Running the module main once is fine. However, when I want to run it again, the process gets killed. A new start of Ubuntu allows running the module once again. I consider this a problem of a to few memory. 

**Idea:** We could go around this problem by running the script on the server. 
The same applies for the module load_and_test





Task 5
--------- 

### Virtual Environments and Requirement File

We installed successfully virtualenv with the below command as this was the first step in an instruction we found online (we encountered a challenge here, as the first instruction to install did not work, the command was `apt-get install python-virtualenv` and the following error message appeared: 

```
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied) E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
```

A second instruction that we found suggested to use `sudo apt install python3-ven`. As we did not want to use any sudo commands, we looked further and found the below command (that worked):
`pip3 install virtualenv`

Next we executed the below command, according to the instruction the following happens once this command is executed: 
Creates a folder that houses the necessary Python executables in the bin directory. 
In this instance, we are installing Python 3.5 while also creating two folders, the virtualenvironment, and project_1 directory. 
Virtualenv will create the necessary directories in the project_1 directory. In this directory you’ll find bin, include, lib, local and share.

```
virtualenv -p /usr/bin/python3 virtualenvironment/project_1
```

Next moved to the bin folder:

```
ls
cd virtualenvironment
cd project_1
cd bin
```

With the following command we noticed as announced in the instruction a change in the terminal, every line started now with (project_1): ``source activate``

With the following command one can exit again the virtual environment: ``deactivate``

Next we decided to test this virtualenvironment out by cloning our files from our github repository with the following command:

```
git clone https://github.com/adrianmrozo/ds.git
```

Which worked. Then.

``
git switch workon
``

To switch to the desired branch. Next we tried to run the code. Now it should not work, as we did not yet install any packages in the virtual environment:

``
python3 cifar10_cnn.py
``

As anticipated, it did not work. Next we tried the following command to install the needed packages by using the requirements.txt file, as to an instruction we found online:

```
pip install -r requirements.txt
```

The installations were processed, however these error messages were shown:

```
ERROR: After October 2020 you may experience errors when installing or updating packages. This is because pip will change the way that it resolves dependency conflicts.

We recommend you use --use-feature=2020-resolver to test your packages with the new resolver before it becomes the default.

tensorflow 2.3.1 requires numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.2 which is incompatible.
```

However at the end the following message was displayed:

```
Successfully installed absl-py-0.11.0 astunparse-1.6.3 cachetools-4.1.1 certifi-2020.6.20 chardet-3.0.4 gast-0.3.3 google-auth-1.22.1 google-auth-oauthlib-0.4.2 google-pasta-0.2.0 grpcio-1.33.2 h5py-2.10.0 idna-2.10 keras-2.4.3 keras-preprocessing-1.1.2 markdown-3.3.3 numpy-1.19.2 oauthlib-3.1.0 opt-einsum-3.3.0 protobuf-3.13.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 pyyaml-5.3.1 requests-2.24.0 requests-oauthlib-1.3.0 rsa-4.6 scipy-1.5.3 six-1.15.0 tensorboard-2.3.0 tensorboard-plugin-wit-1.7.0 tensorflow-2.3.1 tensorflow-estimator-2.3.0 termcolor-1.1.0 urllib3-1.25.11 werkzeug-1.0.1 wrapt-1.12.1
```

As it confirmed that keras 2.4.3 and tensorflow 2.3.1 were installed, we decided to try to run our code again:

```
python3 cifar10_cnn.py
```

It ran successfully, it again started to train a model

```
Epoch 1/100
 430/1563 [=======>......................] - ETA: 1:46 - loss: 2.0861 - accuracy: 0.2135
```

***Conclusion:*** We successfully created virtual environment. Our requirements.txt worked and it downloaded exactly the versions as we specified in the requirements.txt file (to be verified if it was maybe just coincidence and these versions were maybe just the most up-to-date ones). 

And we were able to run our code in the virtual environment with only 2 command lines. So we see the advantage of a requirements.txt file, to simplify an installation. We should at next opportunity, look into the error message, it looks like it would be better if we have a numpy version between 1.16.0 and 1.19.0, at a first sight, it appears that the easiest solution would be to define this also in the requirements file, so that the proper numpy version gets installed in a very first step.

[Used sources and instructions](https://www.liquidweb.com/kb/creating-virtual-environment-ubuntu-16-04/)




Task 6: 
-----------

### Introduction to Docker

1.) **Install docker:**

Start the terminal and follow the steps describes [here](https://docs.docker.com/engine/install/ubuntu/) namely: 

```
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
then

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

followed by 
```
$ sudo apt-key fingerprint 0EBFCD88
```
and 
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
----
Or as **another approach**:
```
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

and 

```
$ apt-cache madison docker-ce
```
 This displays a list of available versions like: 

```
docker-ce | 5:18.09.1~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 5:18.09.0~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 18.06.1~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 18.06.0~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  ...
```
We now need the version string for the respective machine. Get version string type via `$ lsb_release -a`

Copy the version string and type: 

```
install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

Now docker should be installed. However, we can check with one or both of these lines
```
$docker --version 
$sudo docker run hello-world
```
Now Docker is installed. Success! 




With the following we managed that we do not have to use sudo when working with Docker, found on the Docker.com website: 

```
sudo groupadd docker

sudo usermod -aG docker $USER

newgrp docker

docker run hello-world
```



***Get started with Docker Compose***
Next we have followed the Docker instruction "Get started with Docker Compose" (see https://docs.docker.com/compose/gettingstarted/)


<u> Step 1: Setup </u>

```
$ mkdir composetest
$ cd composetest
```

This folder we have just used in the beginning for test purposes, later we transferred the files directly into the main folder.
We created a file called app.py in your project directory and pasted this in:

```
    import time

    import redis
    from flask import Flask

    app = Flask(__name__)
    cache = redis.Redis(host='redis', port=6379)

    def get_hit_count():
        retries = 5
        while True:
            try:
                return cache.incr('hits')
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    raise exc
                retries -= 1
                time.sleep(0.5)

    @app.route('/')
    def hello():
        count = get_hit_count()
        return 'Hello World! I have been seen {} times.\n'.format(count)
```

(In this example, redis is the hostname of the redis container on the application’s network. We use as in the instruction the default port for Redis, 6379.)

As in the instruction we created another requirements.txt in your test and paste this in:

```
    flask
    redis
```

(We later added below the merged this requirements with our already existing requirements file)

<u> Step 2: Create a Dockerfile </u>

In this step, we wrote a Dockerfile that builds a Docker image. The image contains all the dependencies the Python application requires, including Python itself.

In our test directory, we create a file named Dockerfile and pasted the following:
```
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

As written in the instruciton, this tells Docker to:

Build an image starting with the Python 3.7 image.
Set the working directory to /code.
Set environment variables used by the flask command.
Install gcc and other dependencies
Copy requirements.txt and install the Python dependencies.
Add metadata to the image to describe that the container is listening on port 5000
Copy the current directory . in the project to the workdir . in the image.
Set the default command for the container to flask run.

I (Adrian) later noticed this line defining Python Version 3.7 caused a lot of problems, more about these problems will be written later. But we already would like to note down, how this file was changed:

```
FROM python:3.8.3
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

For more information on how to write Dockerfiles, see the Docker user guide and the Dockerfile reference.

<u> Step 3: Define services in a Compose file </u>

We created as written in the instruction a file called docker-compose.yml in your project directory and paste the following:

```
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

This Compose file defines two services: web and redis.
Web service

The web service uses an image that’s built from the Dockerfile in the current directory. It then binds the container and the host machine to the exposed port, 5000. This example service uses the default port for the Flask web server, 5000.
Redis service

The redis service uses a public Redis image pulled from the Docker Hub registry.

<u> Step 4: Build and run your app with Compose </u>

 From our test directory, we started up your application by running docker-compose up.
 
```
$ docker-compose up
```
Compose pulls a Redis image, builds an image for the code, and starts the services you defined. In this case, the code is statically copied into the image at build time.

We entered http://localhost:5000/ in the browser to see the application running.

One can also try http://127.0.0.1:5000.

If you’re using Docker Machine on a Mac or Windows, use docker-machine ip MACHINE_VM to get the IP address of your Docker host. Then, open http://MACHINE_VM_IP:5000 in a browser.

And we see a message in your browser saying:
    Hello World! I have been seen 1 times.
With refreshing the page, the number should increment.

    Hello World! I have been seen 2 times.

    hello world in browser

<u> Step 5: Edit the Compose file to add a bind mount </u>

Edit docker-compose.yml in your project directory to add a bind mount for the web service:

```
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_ENV: development
  redis:
    image: "redis:alpine"
```
The new volumes key mounts the project directory (current directory) on the host to /code inside the container, allowing you to modify the code on the fly, without having to rebuild the image. The environment key sets the FLASK_ENV environment variable, which tells flask run to run in development mode and reload the code on change. This mode should only be used in development.


<u> Step 6: Update the application </u>

Because the application code is now mounted into the container using a volume, we can make changes to its code and see the changes instantly, without having to rebuild the image.

For example, we changed the Hello World! message to Hello from User!:

```
return 'Hello from User! I have been seen {} times.\n'.format(count)
```

We closed it again with the following comand:

```
$ docker-compose down --volumes
```

As this worked now, we started to try out our code with docker with the:

```
docker exec [containerID] python3 [ourfilename]
```

command. It took us quite some time and error messages, until we realized that I have to set the Python version in Docker according to our requirement in our README.md file, see above. 

We also realised that we again needed additional packages, which was more obvious to us, and it worked to install them on Docker and even add them into the requirements.txt file which will be automatically loaded and installed once a docker-compose up is executed.

While the standard CIFAR10 code was running in Docker once the Python version was correct and all the Python packages installed, our modified and modulized code that also was loading and testing the model was not working. After some research of the error message we had to execute the following commands in our Docker, and install 2 more packages manually (but which we added to the requirements.txt file)

```
docker exec f26f900647a3 apt-get update
docker exec f26f900647a3 apt-get install libgl1-mesa-glx libjpeg62
```




