# Project Report

## Milestone 5
Group: Adrian Mrozowski & Ludwig Kraft
Date:  January 9, 2021


Task 0
---------
### Clean up & catch up

WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
To do for final deliverable
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW


Task 1
---------
### How to ... build a data-driven product?
 
#### <u> How can you train a predictive model? How could you manage experiments, and create reports/visualizations while training your model?
Training a CNN can be achieved in Python with the packages TensorFlow and Keras. 

![Introduction to Multilayer Neural Networks with TensorFlow's Keras API | by  Lorraine Li | Towards Data Science](https://miro.medium.com/max/1000/1*LkKz4wtZNBo5i-Vc8DWhTA.png)

For one striving example of a predictive model, check the full project code in our [git repository](https://github.com/adrianmrozo/ds/blob/master/cifar10_cnn.py).

We can manage our experiments by creating reports, and visualizations while training our models. One of those project management softwares is [Weights & Biases](https://wandb.ai/site). Information provided in 'wandb' can help understanding the used parameters for a run some time in the past, to examine performance and compare data, program efficiency, ect...

![](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5dd6bf8f70b529e8c201ea93_s_92F7A2BE132D5E4492B0E3FF3430FFF0FB2390A4135C0D77582A2D21A2EF8567_1574117851346_Screenshot%2B2019-11-18%2B14.57.27.png)



For a practical example on how to use  Weights & Biases, check out Task 2 in Milestone4 [here](https://github.com/adrianmrozo/ds/blob/master/reports/project4.md).


#### <u> How can you improve collaboration in a team?
Even though the answer appears - as so often - to be 42, in this case we talk about **GitHub** and **Version Control**.

 [Github](https://github.com/) is a free, web-based code hosting platform for version control and collaboration. 
![The Best Alternatives to Github – CloudSavvy IT](https://www.cloudsavvyit.com/thumbcache/0/0/85f60b663104f044ba4840ed62faeefe/p/uploads/2019/10/ba9a7cbd.png)

It allows multiple software engineers to work together on a single project without informing all other engineers about each and every minor change in the code. 
Also, Github helps to improve collaboration by avoiding loss of code: Code never is uploaded by updating the code and deleting the old version, but rather in a way, that allows to save all former updates and make them accessible with time stamps of the upload date.

![Version Control Systems: Git, SVN, Mercurial, Bazaar](https://webinerds.com/app/uploads/2015/10/A-Brief-Timeline-of-Version-Control-Systems-03-770.png)


Additionally, we can talk about an easy-to-use, easy-to-set-up, fast, save and practical communication tool. For this class we were introduced to **Slack**, which met all previously mentioned demands.

![Slack New Logo transparent PNG - StickPNG](https://assets.stickpng.com/images/5cb480b85f1b6d3fbadece78.png)


As this question about improvement of team collaboration is asked rather **openly and therefore interpretable**, we want to at least mention some collaboration, soft-skill and leadership based techniques as ...

- setting short-, mid- and longterm goals as well as milestones. Personally as well as for the team.
- personally formulated motivation letters, on why a person is working at a particular task
- events for maintaining and improving team spirit and team awareness (admittedly a rather non-pandemic-feature)
- setting clear, but flat decision hierarchies
- improving response time on personal requests (obviously well improved in today's age of mobile communication)
- improving personal communication (how do I communicate such that I cannot be missunderstood by my auditorium; how to give feedback; how to forumlate critics in an appreciating manner)
- etc...


#### <u> How would you assess and ensure the quality of your code?
<u>**1. Stage:** Does the code work?</u> 
Run the code and check if everything is at least working properly. If the code does what it is supposed to do, the first assessment step is achieved.

<u> **2. Stage:** Readable Code? </u>
Good code should be readable like a prosa sentence or a book (preferably not Schiller or Shakespear). Developers might want to dig into the code to improve it, change it or re-use it. Therefore it'd be great if the code was easy (or at least 'possible') to read and understand. 
Comparing python code with prosa the 'big book of grammar' would be PEP8, which is also available [here](https://www.python.org/dev/peps/pep-0008/).

<u> **3. Stage:** Resources of the Code and Code Efficiency? </u>
How expensive is the code in terms of binded memory and time? 
Computations are generally expensive and we want to design code, that keeps cost for running the code low. Therefore we can examine the code for its general structure: Can we delete unneccessary loops or inefficient memory usage? Can we redesign the code structure to reduce the cost in [O-terms](https://en.wikipedia.org/wiki/Time_complexity)?


#### <u> How can you provide data to the model at inference time and save its predictions to analyze the model’s performance in a real-world scenario?
One of the big problems in a real-world scenario is, that data is generally confidential and can therefore not be detached from the companies security environment. This means, that we - as external consultants or service operatives need to train a model before we get into the real-world scenario and check the results of our model with the real-world data. 

Thus we want to provide data to the model before the "show time" and want to safe the training performence. 

For example, we can provide data to the model with already existing data sets. 

In our case: [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) 
We implemented the loading of the data in the module 'load_and_test' with the simple lines: 

    from prep_cifar10 import prepare_data
    x_train, y_train, x_test, y_test = prepare_data()
![Image Classification on CIFAR-10 Dataset · Image Classification](https://rishabhjain.xyz/ml-class-project/public/images/cifar-10.png)


We can save the model's performance for multiple input parameters for example by tracking the training und test runs with Weights & Biases.

![Partner with ODSC West 2019 -old | Open Data Science Conference](https://odsc.com/wp-content/uploads/2019/03/wandb.png)


#### <u> How can you improve on the model iteratively and deploy it to customers in a web application. How could you structure your product as a microservice architecture?

When training a model, this happens iteratively by completing multiple epochs. The CNN generally improves its performence step-by-step. 

Example: Our CNN gets to 75% validation accuracy in 25 epochs, and 79% after 50 epochs.

How many epochs we run, can be decided individually by setting the according meta variable. However, the performence converges and is not necessarily strictly monotonous (meaning, that even with 1000 epochs we might not reach validation accuracy of 90%).
![Higher validation accuracy, than training accurracy using Tensorflow and  Keras - Stack Overflow](https://i.stack.imgur.com/0TfSp.png)

We provide customers our services in Containers. That means - metaphorically speaking - putting a product in form of code into a box and closing the box. Therefore we fix all versions of everything we put into the box, such that even if we take the code out of the box in the future, the code won't be rotten and foul due to updated versions of packages our code depends on. In the real world we call this process Dockerization. We can send our products to customers in those Containers, which are build by Docker, and that can run for eternity. 
![Docker Tutorial Series | by Romin Irani | Romin Irani's Blog](https://miro.medium.com/max/1200/0*S-MMm259cfFJn-_N.png)

#### <u> Step-by-Step process to launch a web-based E-mail spam detector to Customers

Describe the process step by step with the example of an E-mail spam detector. Assume you want to provide a service where customers can send their E-mails to (f.e. a web page where you can upload E-mail text). The service responds with either “Spam” or “No Spam”. Which tools would you use for each step in the process until the response ends up at the customers’ screens? Also describe what metrics you might use to find out whether your model works (f.e. would you focus on Precision or Recall? Etc.) 

#### <u>1. Milestone
#### Building the Spam detector to work locally.

<u> **1. Stage:** Build a Data Set for Training </u>
We would build a dataset consisting of test and training cases. All emails would be classifiyed to be either SPAM (S) or NO SPAM (O). We would label the emails accordingly. The number of cases shouldn't be too low.

<u> **2. Stage:** Clean and Examine the Data </u>
First we would want to clean the data, i.e. removing punctuation and filler words as "and", "the", "of", etc. This is data, that is equal to all english texts and won't make a difference in detecting whether an email is spam or not. 

We now want to extract several features of the data. Therefore we bring words in a base form: "include”, “includes,” and “included” would all be represented as “include”. We endure this cleaning process to properly...

<u> **3. Stage:** Create Word Dictionary </u>
As a next step, we need to create a dictionary of words and their frequency. For this task the training set is utilized. 
In the end, we want to receive an dictionary as output like:
```
[('order', 1414), ('address', 1293), ('report', 1216), ('mail', 1127), ('send', 1079), ...]
```  
Important are the keys of the dictionary as we will later on map an sample email to this dictionary. We call them ***features***. The text "order, order, the report and send!" will be represented with the values [2, 0, 1, 0, 1, 0, 0, 0, ...]

<u> **4. Stage:** Train model </u>
For document checks the python package ***scikit-learn*** is the one of interest.

After a first research there are two classifiers to approach the problem: 1. **Naive Bayes (NB)** and 2. **Support Vector Machines (SVM)**. NB works probibalistic and under the assumption that features (distribution of the number of appearences of words) are independent in all pairs. SVMs are supervised binary classifiers which are very effective when you have higher number of features.

The model is trained on basis of the training set. For project management purposes and handy information on the performence, we could include Weights & Biases into the training and test phase.

<u> **5. Stage:** Check performence </u>
After the model will have performed, we end up a Confusion Matrix of the following form: 


|     <u>SMV</u>   | **Ham**    | Spam  |
| --------- |:--------:| -----:|
| **Ham** (actual)    | 197| 3 |
| **Spam** (actual)   | 6     |  194  |


**Notes:** Ham is the counterpart of spam emails, i.e. non-spam or regular mails.

This particular confusion matrix would state, that we have an

$Accuracy=97.75\%$
$Precision=97.04\%$
$Recall=98.5\%$

These were pretty good values. Thinking about how to rate the performence of the model, it is obvious that the Accuracy is paramount. A higher number of correctly classified cases is better than less. 
However, to examine the model even closer we ask, whether it is more important to not lose Hams to the Spam (which means, good mails are incorrectly classified as Spam, which is a prosa description of Precision) or whether it is more important not to receive incorrectly Ham classified Spam mails, which is expressed by the Recall). 

Obviously we value it higher not to lose potentially important information to the spam filter than deleting a spam mail, that made it into the inbox from time to time. 

**Thus we would want to specialise the spam filter according to Accuracy and Precision.** 

We would even be positive to trade-off some Recall points for better precision.

Now our product is working nice and well and we are ready for packaging and delivery. 


**Notes:**
Great [video](https://www.youtube.com/watch?v=exHwwy9kVcg) and [blog source](https://www.kdnuggets.com/2017/03/email-spam-filtering-an-implementation-with-python-and-scikit-learn.html) to learn about implementation of a spam detector.


#### <u> 2. Milestone
#### Make product available online and secure it for eternity.

<u> **1. Stage:** Dockerize code </u>
We dockerize our code using [Flask](https://flask.palletsprojects.com/en/1.1.x/) as our web application framework. 

<u> **2. Stage:** Beauty adjustments </u>
As the spam filter is up and running in a container and the performence is optimized to our convenience, we want to make the product look nice. So, we work with flask to make the interface look better, maybe use some colors and a cool logo for our groundbreaking new peice of techology. Now print flyers, tell your grandparents about your work and advertise in the local newspaper: This new spam filter is now available on this omnious place called "the internet".

<u> **3. Stage:** Up and Running </u>
We now need to "go live" with our application. We use gunicorn as WSGI Server (run our docker container there) and NGINX as web server (we can access the web application with our web browser over this path).





Task 2
---------

### Implementation

#### First Idea

The first sub-task was once more to understand the instructions of the task. 

As dealing with Flask for educational purpose in Milestone 3 for learning how to the setup the .yml file to use docker-compose is some time in the past already, I refreshed my knowledge quickly with a [great flask tutorial](https://www.youtube.com/watch?v=s_ht4AKnWZg) from a great indian teacher. 

Here I understood the first specification of the task (*"Accept a HTTP POST Request at 'localhost:<port>/predict'"*)

Here the basis on which I started to understand this part: 

    from flask import Flask, jsonify, request
    
    app = Flask(__name__)
    
    @app.route("/", methods = ["GET", "POST"])
    def index():
        if (request.method == "POST"):
            some_json = request.get_json()
            return jsonify({"You sent": some_json}), 201
        else:
            return jsonify({"about":"Hello World!"})
    
    @app.route("/multi/<int:num>", methods =["GET"])
    def get_multiply10(num):
        return jsonify({"result": num*10})
    
    
    if __name__ == '__main__':
        app.run(debug=True)


Whenever we will type in the running web browser 

    http://localhost:<port>/predict
    
we want to see an image pulled from the Cifar-10 and a label predicted by our CNN.

What's to do? In my own words: 
We set up a container for the web application with Flask, that has the service 'predict'. This service should load a .h5 model and contain a sample of the dataset. That should be done with an .yml file.

When requested by an extra python script, the container tests the sample with the CNN and stores the image AND the predicted label in a postgresql database, which runs in another container. The image and predicted label should then be printed in the console. 

We need: 
- .yml file to start Flask (with second service postgres)
- python code to request sample test.


tbc
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW


#### Second Idea

Make the overall project run on Colab without minding the virtual environment and docker container. Then dockerize the working code in a second step. 

We based our try and error procedure on the jupiter notebook of our latest Milestone4. Follow along [here](https://colab.research.google.com/drive/1z95gJROm3aU2PaN4z1jZooFMTTbeSMz-?usp=sharing#scrollTo=A0HE4AbMjj0b)




tbc
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

























-----
# THE END 




