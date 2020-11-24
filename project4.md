
# Project Report

## Milestone 4
Group: Adrian Mrozowski & Ludwig Kraft
Date:  November 27, 2020



Task 1
---------
### Introduction to Weights & Biases 
Creating an account on [Weights & Biases](https://www.wandb.com/) is working straight forward with an pre-existing github account. 

I started out with the tutorial [Keras with W&B](https://colab.research.google.com/drive/1pMcNYctQpRoBKD5Z0iXeFWQD8hIDgzCV#scrollTo=Lxjw5Qckzg5W) to get an idea of how W&D is working and how our end result of this milestone should actually look like. 

### Vocabulary

#### <u> What is Experiment Management and why is it important?
Projects in general, but machine learning projects in particular are challenging tasks to complete. Not only because of its complexity and enourmous required skill level, but also because of the sheer number of variables, datasets and artifacts to track and manage.

As a developer or data scientist, we do not want to spend much time managing spreadsheets or databases to track experiments, datasets and their relationships with each other.

Questions get raised as: What dataset, training scripts and model hyperparameters were used for a model that you trained a week ago? a month ago? a year ago? 

To find an answer to this question, we can look through your notes, audit trails, logs and Git commits, and try to piece together the conditions that resulted in that model. Still we cannot be sure whether we changed some parameters manually. 

The solution is to use Experiment Managenent Tools. It is a ***5-step process***, that should be explained in the following:


#### Step 1: Formulate a hypothesis and create an experiment

The first step is to define your hypothesis. This enables us to evaluate out whether the experiment on a later stage and helps finding back on the right track, in case we get lost.

#### Step 2: Define experiment variables

An experiment includes a list of variables that you vary across a number of trials. These variables could be hyperparameters such as batch size or some other factor that you think can have an effect on the response i.e. accuracy or loss for CNNs.
Create several lists with variation in the parameters.

#### Step 3: Tracking experiment datasets, static parameters, metadata

Before launching several experiment trials and training models for each of the hyperparameter options in Step 2, I have to make sure that I also track artifacts and parameters that are common across trials. I.e. Static hyperparameters like batch-size. Also training, validation and test datasets.

#### Step 4: Create Trials and launch training jobs

In this step we loop through the variable sets created in Step 2 and create a trial and a training job for each set.

#### Step 5: Analyzing Experiment results

After the training jobs have finished running, we can now compare all the Trial runs and draw inferences about the Experiment. We can use this data to either accept or reject the hypothesis that the new model delivers better accuracy for a dataset.

For more detailed information on Experiment Management, check e.g. this [blogpost](https://towardsdatascience.com/a-quick-guide-to-managing-machine-learning-experiments-af84da6b060b).

#### <u> What is a Metric in ML?

Metrics are being used to monitor and measure the performance of a ML model. 

The performance of ML algorithms that are measured and compared depends entirely on the chosen metric. This means that one ML model can get measurements that vary widely depending on the very metric used. 

To compare the idea: We can also evaluate an English text according to the correct grammar, its level of vocabulary, number of letters or number of occurrences of the letter "a", number of rhyming words, ect. Depending on which criteria we use for evaluating the text, we get different outcomes.

 
#### <u> What is a Confusion Matrix?

The Confusion matrix is a metric that is used for Classification problems where the output can be of two or more types of classes. It gives a matrix as output and describes the complete performance of the model.


The output in a binary classification problem consists of a 2x2 matrix with 4 important terms:
![Image for post](https://miro.medium.com/max/1380/1*0exdQRxrXQgIBZdPFIxbTw.png)

**1. True Positives (TP):**  True positives are the cases when the actual class of the data point was 1(True) and the predicted is also 1(True)

**2. True Negatives (TN):**  True negatives are the cases when the actual class of the data point was 0(False) and the predicted is also 0(False)

**3. False Positives (FP):**  False positives are the cases when the actual class of the data point was 0(False) and the predicted is 1(True). False is because the model has predicted incorrectly and positive because the class predicted was a positive one. (1)

**4. False Negatives (FN):** False negatives are the cases when the actual class of the data point was 1(True) and the predicted is 0(False). False is because the model has predicted incorrectly and negative because the class predicted was a negative one. (0)

The ideal scenario that we all want is that the model should give 0 False Positives and 0 False Negatives. But that’s not the case in real life as any model will NOT be 100% accurate most of the times.

A much more detailed description of the Confusion Matrix can be found [here](https://medium.com/@MohammedS/performance-metrics-for-classification-problems-in-machine-learning-part-i-b085d432082b).

<u>*Confusion Matrix forms the basis for the other types of metrics.*</u> 
For example: Accuracy is an output variable in our CNN, too. 
It is defined as 

$Accuracy = \frac{TP+TN}{TP + FP + TN + FN}$ 

That is the number of correctly classified tests per all tests done.  


#### <u> What is Precision and Recall? Why is there often a Trade-off between them?
Both matrics can be deducted from the Confusion Matrix - just like Accuracy. 

$Precision = \frac{TP}{TP + FP}$ 	

Precision is a measure that tells us what proportion of tests that we classified as 1(True), actually are 1(True). It describes the percentage of correctly classified cases of all positively classified test cases. We ask: "How many correct cases did we catch?"

$Recall = \frac{TP}{TP + FN}$ 

Recall is a measure that tells us what proportion of tests that actually are 1(True) were classified by the algorithm as 1(True). It describes the percentage of correctly classified cases of all actual positive test cases. We ask: "How many correct cases did we miss?"

Why is there a Trade-Off between the two? 

Precision checks the correct classification of all positively classified cases. If we only catch one correct case and it is correctly classified as correct, we get an Precision of 100%.

Recall checks the number of missed cases. If we classified every single case as correct, we would also catch all available positive cases and therefore get an Recall of 100%.

Thus, if we want to focus on minimising False Negatives, we would want our Recall to be close to 100% without precision being too bad. If we want to focus on minimising False positives, then our focus should be to make Precision close to 100%.

#### <u> What is AUROC Metric?

The AUROC (synonyms: AUC, ROC) metric 
is a metric, that is also based on the confusion matrix. It stands for "Area Under the (Curve)"(AUC), "Receiver Operating Characteristics"(ROC). 
There ROC is a probability curve and AUC represents degree or measure of separability.

<u> AUC </u>
Is the AUC value equal to 1, the model is working perfectly and making no mistakes. An AUC value of 0 is the worst and the model is classifying every single case incorrectly. For a 0.5 value the model is simply guessing and getting 50% of the cases correctly (given that there the classes have the same size). 

![](https://miro.medium.com/max/1014/1*yF8hvKR9eNfqqej2JnVKzg.png)

Here the red distribution curve is of the positive class(1, True) and green distribution curve is of negative class(0, False). The better the model, the smaller the shared area of both distributions becomes. Ideally they only touch at the threshold (AUC = 1). For an model, that does only guess randomly (AUC = 0.5) both distributions would overlap completely and share their highpoint at the threshold.

<u> ROC </u>

The ROC is being plotted with TPR (True- Positive-Rate = Recall) against the FPR (False-Positive-Rate). We have

$FPR = 1-Specificity =\frac{FP}{TN + FP}$

where $Specificity = \frac{TN}{TN + FP}$

Specificity tells us what proportion of the negative class got correctly classified.

![roc-curve-v2](https://glassboxmedicine.files.wordpress.com/2019/02/roc-curve-v2.png?w=616)

One notices immediately, that with a perfect classifier the Area Under the Curve (AUC) equals to 1. For a random classifier exactly half. 

The positively monotonous ROC curve therefore states: 
The higher the Rate of False Positives, the higher the Recall. Meaning, the more False cases we classified as True, the more tests that are True were classified correctly as such.









---
---
---

Task 2
---------
### Implementation

I started out with the tutorial [Keras with W&B](https://colab.research.google.com/drive/1pMcNYctQpRoBKD5Z0iXeFWQD8hIDgzCV#scrollTo=Lxjw5Qckzg5W). 
When installing new packages, I immediately added them to the requirements file of the local development folder. 
```
wandb == 0.10.11
opencv-python == 4.4.0.46
``` 

get started with wandb:
https://docs.wandb.com/quickstart















Task 0
---------
### Clean up & catch up

As kindly provided by Arthur the last feedback sheet made us aware of a few points that weren't completed in their entirety within the setting of the last milestone. We want to solve the remains in this section. 

#### <u>PEP8 conformity
Ludwig noticed that there were indeed several names set incordantly with PEP8. I quickly changed names like folder names with upper case initial letter to lower case letters (e.g. "Modules" -> "modules").

More importantly there several script names and function names needed to be modified. Check several examples vicariously: 

<u>script names: 	
- setInitials &rarr; set_initials 
- shapeModel &rarr; shape_model 		





-----
# THE END 


















----

### Notes: 

Commands used in the research for this task. Saved here for future use: 

-  Created a account on docker hub and login in terminal via: 
``docker login`` and credentials
- shorten command line standard line via `export PS1="\u$ "`

***docker images***
- `docker images` to view all images locally available 
&#8594; check versions  `-a` for checking all information there is and `-q` for requesting only the image IDs

-----
---
