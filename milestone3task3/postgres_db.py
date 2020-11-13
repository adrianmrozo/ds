host = "127.0.0.1"
database = "postgres"
port = "5432"
user = input("Insert a name for your database:") or "postgres"
password = input("Insert a password for your database:") or "pgpass"

import psycopg2
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os

batch_size = 32
num_classes = 10
epochs = 100
data_augmentation = True
num_predictions = 20
save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'keras_cifar10_trained_model.h5'

# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

trainimages=(x_train)
testimages=(x_test)


con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

cur = con.cursor()

cur.execute("CREATE TABLE input_data (ID SERIAL PRIMARY KEY, image INTEGER);")

cur.execute("insert into input_data (ID, image) values (%s, %s)", (1, len(testimages[1])) )

#execute query
cur.execute("select image from input_data;")
print ("This is the saved picture:")
print(cur.fetchall())


#commit my input data to db
con.commit()




con.close()
