host = "127.0.0.1"
database = "postgres"
port = "5432"
user = input("Insert a name for your database:") or "postgres"
password = input("Insert a password for your database:") or "pgpass"

import psycopg2

con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

cur = con.cursor()


cur.execute("CREATE TABLE jokes (ID SERIAL PRIMARY KEY, joke TEXT);")

cur.execute("insert into jokes (ID, joke) values (%s, %s)", (1, "Warum freut sich eine Blondine, wenn sie nach 6 Monaten ein Puzzle geschafft hat? - Weil auf der Verpackung steht: 2-4 Jahre.") )

#execute query
cur.execute("select joke from jokes;")
print ("This is my favorite joke:")
print(cur.fetchall())


#commit my input data to db
con.commit()


con.close()
