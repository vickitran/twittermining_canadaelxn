import MySQLdb
import sys

#mysql.server start
#mysql -u root -p
#CREATE DATABASE dbname;
#USE dbname;
#CREATE TABLE tables (Username VARCHAR(20), Tweet VARCHAR(140), Time INT(13), NDP INT(13), Conservative INT(13), Liberal INT(13)); 

# connect to database (server, MySQL username, MySQL pass, Database name)
try:
	conn = MySQLdb.connect("localhost","root","cookies","root$tutorial")
except Exception as e:
	sys.ext('We cant get into the database')

# cursor used to execute queries
c = conn.cursor()

'''
try:
	c.execute("CREATE TABLE  (username VARCHAR(20), tweet VARCHAR(140), time INT(13), ndp INT(13), conservative INT(13), liberal INT(13))")
	conn.commit()
except Exception as e:
	sys.ext('Database already exists')
'''

# insert a row into table
def insertRow(user, tweet, time, freqNDP, freqCons, freqLib):
	# execute specified query: 
	c.execute("INSERT INTO tables (username, tweet, time, ndp, conservative, liberal) VALUES (%s,%s,%s,%s,%s,%s)",
            (user, tweet, time, freqNDP, freqCons, freqLib))

    # commit changes to database
	conn.commit()

	return True

# produces sum of specified party
def getSum(party):
	c.execute("SELECT SUM(%s) FROM tables", [party])
	#result = c.fetchone()
	#print result
	return True
