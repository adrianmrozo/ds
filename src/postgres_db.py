#host = "127.0.0.1"
#database = "milestone5"
#port = "5005"
#user = input("Insert a name for your database:") or "postgres"
#password = input("Insert a password for your database:") or "pgpass"


host = "postgres"
database = "milestone5"
port = "5432"
user = "postgres"
password = "pgpass"

import psycopg2
import numpy as np

con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)
cur = con.cursor()

# create input data table
cur.execute("CREATE TABLE input_data (ID SERIAL PRIMARY KEY, input_label TEXT, image TEXT, predicted_label TEXT);")
con.close()


#store test data, test label, prediction label

def savingtestresult(test_label, test_data, pred_label):

    host = "postgres"
    database = "milestone5"
    port = "5432"
    user = "postgres"
    password = "pgpass"

    con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)
    cur = con.cursor()

    #savingtestresult.counter += 1
    #load testdata into database input_data
    cur.execute("insert into input_data (ID, input_label, image, predicted_label) values (%s, %s, %s, %s)", (1, test_label, str(test_data), pred_label))

    #execute query
    #cur.execute("select * from input_data;")
    #image1 = np.fromstring(cur.fetchall()[-1], dtype = int).reshape(32,32,3)
    #print ("These are the inputs that have been tested so far:")
    #print(cur.fetchall()[-1], image1)

    #cur.execute("select * from predictions;")
    #print ("The CNN predicted the tested inputs to be:")
    #print(cur.fetchall())
    #commit data to db
    con.commit()
    con.close()
#savingtestresult.counter = 0

