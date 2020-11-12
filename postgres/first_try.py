import psychopg2

#connect to db
con = psycopg2.connect(
	host = "kraftl", #host name postgres admin or kraftl
	database = "postgres_db", #database name
	user = "kraftl",
	password = "myfirstdb")
	
cur = con.cursor()

sur.execute("insert into <dbname> (<col.name1, col.name2>), values (%s, %s)", (1, "<name>") )

#execute query
cur.execute("select <col.name> from <dbname>")

rows = cur.fetchall()

for r in rows: 
	print (f"<col.name>{r[0]} col.name2> {r[1]}")

#commit my input data to db
con.commit()

#close cursor
cur.close()


#close the connection to database
con.close()
