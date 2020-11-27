
# Project Report

## Milestone 4
Group: Adrian Mrozowski & Ludwig Kraft
Date:  November 27, 2020


Task 0
---------
In case we do not manage to complete task 0 (correct and complete the last milestone) we have accepted our lecturers offer to complete it in a later stage after our exams.

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

$$Accuracy=\frac{TP+TN}{TP+FP+TN+FN}$$

That is the number of correctly classified tests per all tests done.


#### <u> What is Precision and Recall? Why is there often a Trade-off between them?
Both matrics can be deducted from the Confusion Matrix - just like Accuracy. 

$$Precision=\frac{TP}{TP+FP}$$

Precision is a measure that tells us what proportion of tests that we classified as 1(True), actually are 1(True). It describes the percentage of correctly classified cases of all positively classified test cases. We ask: "How many correct cases did we catch?"

$$Recall=\frac{TP}{TP+FN}$$

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

$$FPR=1-Specificity=\frac{FP}{TN+FP}$$

where $$Specificity=\frac{TN}{TN+FP}$$

Specificity tells us what proportion of the negative class got correctly classified.

![roc-curve-v2](https://glassboxmedicine.files.wordpress.com/2019/02/roc-curve-v2.png?w=616)

One notices immediately, that with a perfect classifier the Area Under the Curve (AUC) equals to 1. For a random classifier exactly half. 

The positively monotonous ROC curve therefore states: 
The higher the Rate of False Positives, the higher the Recall. Meaning, the more False cases we classified as True, the more tests that are True were classified correctly as such.








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

As all efforts to complete the task with the docker login failed, we left out the adaption of the requirements file as it was unneccessary. 

Regarding the task: "Choose an appropriate metric to optimize your model". The most straightforward metric was the "accuracy" with which our trained models is able to predit a category (1 out of 10) if a picture is shown to it. I cannot think of any other metric that would make sense in this context: Of any other metric taht would measure the performance of our model better.

Surprisingly task 2 went quite smooth. We approached task 2 as suggested, we created first an account (for simplicity reason we registered directly with our Github account) and started to research how we can combine WANDB with the CIFAR 10 dataset. We found a lot of sources on WANDB itself, which showed very easy and fast implementations, however they used Pytorch, we according to our knowledge is not used in our code. We also tried out the wandb "magic one line of code", which surprisingly indeed worked and created entries on our account on wandb.com. Afterwards we found however the most helpful instructions, once we clicked on "new project" on the website and they showed instruction how to implement wandb in our code if we use Keras. And it indeed worked. In order to not complicate things again with Docker, we approached task 2 for starters with the original cifar10_cnn.py file. With the idea once we make it work as planned we will eventually implement it also with Docker. In case we do not make it run in Docker in this milestone, this time we will use our lecturers offer to not use Docker in this time, to save time for exam preparations.

So let's check what we managed to complete:
- *Train a Model:* **Done.** See next line
- *Save and upload the trained model:** **Done.** We trained and saved a model as usually and as we did many times already inthe past milestones, this time with wandb the model was also uploaded into the cloud on www.wandb.com and saved there. The last run at the writing of these words was "wise-dream-4" (interesting names that wandb creates), as the project is public anybody can access the nformation about this training run and also the trained model here: https://wandb.ai/adrianmrozo/test/runs/uaw9b6p0/files?workspace=user-adrianmrozo
- *Log the value of the loss function (graphically):* **Done.** WANDB has done this for us, see here: https://wandb.ai/adrianmrozo/test/runs/uaw9b6p0/files?workspace=user-adrianmrozo wise-dream-4 val_loss 2 was: 1.289
- *Log your metric (graphically)*: **Done.** Wandb.com has done this for us, see here: https://wandb.ai/adrianmrozo/test/runs/uaw9b6p0?workspace=user-adrianmrozo the accuracy for each of the 3 steps/epochs was as follows: 31.05%, 42.9%, 47.47%. Which makes sense that the model became more accurate after every "round of training".
- *Try to play with your Neural Network, by changing parameters*: **Done.** As we had most experience with epochs, we did the most straightforward thing for starters and changed the number from 3 to 20. The code is still running, at the moment at epoch 16 out of 20, but as expected the accuracy already increased to 67%. There are the following parameters that are easy to set: batch_size = 32
num_classes = 10
epochs = 20
data_augmentation = True
num_predictions = 20
As num_classes are in my understanding the number of categories, it would not make any sense to change this, as there are just 10 categories in the CIFAR 10 dataset. epochs we already changed to 20 for the current run. Data_augmentation sounds like changing the setting for the training data set, we expect if we set it to false, that the accuracy rate for the model should decrease, as the training data set will be not augmented anymore. I am not 100% sure what it means and what would happen if we change batch_size and num_predictions. However batch_size sounds rather like the characteristics of the CIFAR 10 dataset (as reminder: The CIFAR-10 dataset consists of 60000 32x32 colour images).
**Update:** The training of the model ended with 20 epochs, and the accuracy indeed increased to 0.6824 or 68.24%. See: https://wandb.ai/adrianmrozo/test/runs/1nj06sad?workspace=user-adrianmrozo
**2. Update:** I also made a run with 3 epochs with "Data_augmentation" set to: False. Interestingly the accuracy became better faster, the accuracies of the 3 epochs from first to the third and last were: 33.95%, 45.62%, 51.34%. Compared to Data_augmentation set to True before the accuracies for 3 epochs were: 31.05%, 42.9%, 47.47%. See: https://wandb.ai/adrianmrozo/test/runs/101qndb6?workspace=user-adrianmrozo
We can think of the following reasons:
- Coincidence
- Maybe the unaugmented and "realer" images were better to train model
For sure one should make a run of more epochs, for example a 100, to determine if this setting really improved the model's prediction power.

Regarding the W&B Login precautions, we did not have to worry so far, as we did not run the code yet as a Docker image. If we find time we will also do thar and run it as a Docker image. So far we just had to past once our wandb code into the terminal.

You can find the file with which all the above was executed so far in the folder milestone4task2(later wandb), with a slightly edited cifar10_cnn.py file. We used the original code and not the modularized one as we messed up our modularized version completely, such that finally nothing worked. Now we present a working solution. 



Task 3
---------

This task reminded me very much in the attempts I did regarding task 2 in milestone 3. I therefore took out again the code that I used back then and pasted it into a Google Colab Jupyter Notebook. I decided to use Google Colab, that even though we have a disadvantage because everything is shared with Google, it is just a bit faster as everything is saved instantously and can be shared in a split second with my team colleague. As time is of the essence. Also as it is not a commercial project we do not mind to share the code with google.

I continued where I ended, and after looking what the dataset is made of inside the numpy.ndarray I saw values like "255" which resembled a colour code, and I was thinking to analyze the colors of the dataset images as an example. I looked into it and tried several things as displaying colors with a matlab function. I even managed to display it but only a grey color came out. I read again (for 100s time) the description of the dataset: "first 32 entries of the array are the red channel" and realised all the values are only the values of the red value, and RGB consists of red, green and blue, so I was missing the green and blue values for this color. I realized that unless I do not put the values together, to have RGB values, it would make little sense to analyze any of the data further. Considering if I should try to attempt that, I remembered that I already stumbled accross a Jupyter Notbook, also in task 2 in milestone 3 that was describing to some extent the data. Even though I did not managed to make it work back then, as I tried to run it locally, this time I was using Google Colab, so I tried to upload the dnn.ipynb file from https://github.com/pranka02/nn_CIFAR10 (I also forked this repository) to Google Colab.

It took quite some work to make it run, as I had to write a little bit of code, that the tar.gz file with the Dataset will be downloaded automatically into a Google folder, so that the rest of the code can be executed. As I wrote in the notebook: In Google Colab, that Cifar 10 package, a tar.gz file, gets downloaded in the "/content/" directory, please adjust in case you do not use Google Colab and it was downloaded in another folder. 

Please find the link here:
https://colab.research.google.com/drive/1NhcaJ3EdpbmZhBch7xkHJg6tL6r0eR3Y?usp=sharing

I recommend to just use this link. Alternatively one can also try to run the file that I added in our repository in the folder "datasetanalysis" (again I would recommend it to just upload it to Google Colab).

At the end the Google Colab Jupyter Notebook worked quite well it displays the dataset quite well and even shows pictures out of the dataset using matlab functions. Interestingly the picture changes everytime I run again the code. I also added my own code in the second half which ended up in a dead end just with the values for the red colors. But also my code uses another approach where the file does not have to be actually downloaded, so it might be still of value in the future, in case we would like to assemble the colors ourselves together again.

Additionally we added a histogramm with numpy and displayed it with matplot. 



-----
# THE END 






