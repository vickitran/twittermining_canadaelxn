'''
database.py
Module to act as a connector to database to store tweets.  Creation of database and table is automated; however, server, user, and password required.
'''

import MySQLdb
import sys

'''
mysql instructions:
mysql.server start
mysql -u root -p
CREATE DATABASE dbname;
USE dbname;
CREATE TABLE tables (Username VARCHAR(20), Tweet VARCHAR(140), Time INT(13), NDP INT(13), Conservative INT(13), Liberal INT(13)); 
'''

# connect to database (server, MySQL username, MySQL pass, Database name)
try:
	conn = MySQLdb.connect("localhost","root","cookies")
except Exception as e:
	sys.ext('We cant get into the database')

# cursor used to execute queries
c = conn.cursor()

# create and use database
c.execute("CREATE DATABASE IF NOT EXISTS root$tutorial")
conn.commit()
c.execute("USE root$tutorial")
conn.commit()

# create table to store tweets
c.execute("CREATE TABLE IF NOT EXISTS tweetTable (username VARCHAR(20), tweet VARCHAR(140), time INT(13), ndp INT(13), conservative INT(13), liberal INT(13))")
conn.commit()

# insert a row into table, parties should only have value of 0 or 1
def insertRow(user, tweet, time, freqNDP, freqCons, freqLib):
	# execute specified query: 
	c.execute("INSERT INTO tweetTable (username, tweet, time, ndp, conservative, liberal) VALUES (%s,%s,%s,%s,%s,%s)",
            (user, tweet, time, freqNDP, freqCons, freqLib))

    # commit changes to database
	conn.commit()

	return True

# produces sum of specified party: ndp, conservative, liberal
def getSum(party):
	stmt = "SELECT SUM({0}) FROM tweetTable".format(party) #assumes column name is trusted input
	c.execute(stmt)
	#c.execute("SELECT SUM(%(party)s) FROM tables", [party])
	result = c.fetchone() #gets the row of the produced sum table
	#return value within the cell
	print result[0]
	return result[0]

#determine percentage of tweets relevent to specific party: ndp, conservative, liberal
def getPercent(party):
	c.execute("SELECT COUNT(*) FROM tweetTable")
	result = c.fetchone() #gets the row of the produced sum table
	percent = getSum(party)/result[0] * 100
	#return percentage
	print "{}{}".format(percent, "%")
	return percent