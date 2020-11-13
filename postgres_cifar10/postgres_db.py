host = "127.0.0.1"
database = "milestone3"
port = "5431"
user = input("Insert a name for your database:") or "postgres"
password = input("Insert a password for your database:") or "pgpass"

import psycopg2
import numpy as np

con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

cur = con.cursor()

# create input data table
#cur.execute("CREATE TABLE input_data (ID SERIAL PRIMARY KEY, input_label TEXT);")

#create predictions table
#cur.execute("CREATE TABLE predictions (ID SERIAL PRIMARY KEY, prediction TEXT);")

#train the model and store it
#also make it available in this script
import main
model = main.model

#store test data, test label, prediction label
from test import test_one
testData, test_label, pred_label = test_one(model)

#load testdata into database input_data
cur.execute("insert into input_data (ID, input_label) values (%s, %s)", (3, test_label) )

#load prediction into database predictions
cur.execute("insert into predictions (ID, prediction) values (%s, %s)", (3, pred_label) )



#execute query
cur.execute("select * from input_data;")
print ("These are the inputs that have been tested so far:")
print(cur.fetchall())


cur.execute("select * from predictions;")
print ("The CNN predicted the tested inputs to be:")
print(cur.fetchall())


#commit data to db
con.commit()


con.close()
