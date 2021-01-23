# <u> Data Science Toolkits and Architectures - A process summary

This repository displays the end product of Adrian Mrozowski's and Ludwig Kraft's efforts of  University Lucernce's program *Data Science Toolkits and Architectures* led by Sandro Cilurzo and Arthur Habicht. 

The program was split into several milestones, which were again divided into multiple subtasks.
The reports in this folder describe the endeavor of our try-and-error process, plunging into the unknown and following paths that did not always lead to the desired result.

Details for each milestone can be found in the corresponding report.

____


## Milestone 1 
We started our machine learning (ML) story by examining both pieces of information that we received for the start of the course: A machine learning python code *cifar10_cnn.py*, which is now stored in "src/legacy/initial_code" and the  [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset. 

#### <u>The Dataset CIFAR-10</u>
Research found that the dataset consisted of a training and a test branch, which together contain 60'000 images of size 32x32 sorted in 10 different and exclusive classes.

The dataset is designed to solve a classification problem of computer recognition and image classification. 

#### <u>The Code</u>
First, we examined the structure of the code and tried to understand, what it does step-by-step.

Then, a big challenge was to make the code run on our own machines and to install several necessary packages and versioned dependencies for Python. We made aquaintence with Keras and Tensorflow and learned about their important role in ML.

We learn that the resulting model is a Convolutional Neural Network (CNN) and its important property to efficiently handle high dimensions of raw data. 

On the question which parameters could we use to rate our CNN, we found out about the output sizes accuracy and loss.


#### <u>Linux Command Line and GitHub</u>
We had to dive into two - at least for us - completely new concepts of using a computer. 
We started our repository, got to know about the utmost importance of code versioning with GitHub for Software Development and set up a README file. 

We abandoned the UI and started using the Linux Command Line. Using ``pip`` and ``git`` commands appeared like learning a new language. We made our first commit and push by playing with ``git branch`` , ``git pull``, ``git add .`` , ``git commit -m "<your-commit-message>"`` and  ``git push``.



## Milestone 2

#### <u>GitHub</u>
We needed to set up a branching strategy. First, it was confusing to properly use different branches, but eventually it became clear how useful the set-up actually is. To keep our repository nice and clean, we set up a .gitignore file. To ensure the quality of our commits, we prohibited direct pushes to the master branch (4-eyes-principle).

#### <u>IT Vocabulary </u>
We learned about hash functions and the difference between python modules, scripts and packages. In this regard the best practice of "modularization" was introduced. PyPi for assessing the quality of a python package.

#### <u>Introduction to Docker </u>
We were introduced to the concept of Docker Containers. The process of writing a Dockerfile, building a docker image, which then results in a container was endured. Docker volumes are used to insert or extract data from containers (mnemonic: box with hole). Using DockerHub to pull images, that somebody already built for us. Docker vs. virtual environments. Why do we need a requirements file and what do we store there?
Then, we installed Docker and built our first Dockerfile, images and containers. Quick outlook on docker-compose.

#### <u>An Attempt of Coding: Modularization </u>
First, we ensured that our code could load data, as well as train, save and load a CNN. Predictions using the model were made as well. Then, we needed to cut our ML code into several autonomous, stand-alone snippets of python code: modules.
The goal is to make code more readable, changeable and workable. "Good code can be read like a story."


## Milestone 3

#### <u>Best Practices </u>
Just like modularization we learned about PEP8 conformity and how to apply it.

#### <u>Another Attempt of Coding: Dockerizing the Modularized Code </u>

How does Dockerizing now practically work with our CNN and the CIFAR-10 dataset? We tried to make our modules run in Docker. Build a Dockerfile and make it to an image, then run the image to create a container. Where are the containers and images listed? How do we run a container?

#### <u>IT Vocabulary </u>
What is Docker-compose and how do we write .yml files? What is a Multi-Docker Application good for? Which roles do ports play? Who is the localhost, that hides behind 127.0.0.1 and - most importantly - why should we not try ``sudo rm -rf`` at ~?

Then, we did some research on the concepts of an SQL Injection Attack, how to protect against SQL injections and what Decompression Bombs are.

Furthermore we learned about PostgreSQL and its importance for building a database


#### <u>Another Attempt of Coding: Postgres and pgAdmin</u>

Display a PostgreSQL database with pgAdmin and put it in a docker container. Then extract one sample. As difficult as the task sounds, it was.
We tried this first with a self-made jokes database and continued with our own dataset. Therefore, we had to think about how to represent/transform image data to save it to the relational database.

This also included rewriting several functions and implementing a completely new module. We also wrote our own .yml files to start the services with docker-compose.



## Milestone 4

#### <u>IT Vocabulary</u>
We were introduced to Experiment Management, which is important to ensure a continual progress in ML projects. An useful tool to to so is Weights & Biases. Amongst others it allows to keep track of the input and output parameters of a model. It is fundamental for optimalization of CNNs to notice differences in outcome after multiple test runs with adjustments in input parameters. How can we talk about optimalization of CNNs in general? Well, we use metrics and, promptly, we were given the opporunity to discover several metrics and how they come into existence: 
The confusion matrix as a metric that describes the complete performance of the model: There, we distinguish between True Positives, True Negatives, False Positives and False Negatives.
We learn about the definition of Accuracy and its differences to Precision and Recall. Why is there often a Trade-off between them? We also learned about the AUROC metric.

#### <u>And some more Coding</u>
We adapted our code such that it would login to weights & biases and ensured that it loged the value of the loss function and the metric graphically.

#### <u>Google Colab and Jupyter Notebooks</u>
We introduced ourselves to the concept of Jupyter Notebooks and used several to try new coding ideas in Google Colab and to easily set up the correct environment for experiments on our python code.


## Milestone 5

#### <u>Putting it all together</u>

In the fifth and last milestone, we put everything we learned together. First, theoretically describing the set-up of a web-based email spam filter and second, practically with our code and data: We built a web application with flask that accepts a POST request for a sample image, returns the predicted class to the user, saves the sample to a postgres database and, finally, displays the predicted image to the user. 


-----
# THE END 






