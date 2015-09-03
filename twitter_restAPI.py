import tweepy 
import codecs # have to encode text before writing to file 
import re # regular expressions 
import string 
from collections import Counter

# tonny's credentials
access_token = "21627027-w4cJ0ugNNFIXzyt3YOj3In2YumXpk28a4K9RszLte"
access_token_secret = "C1kbLxrjjss8M73Dd1CUa8MgUFev2xieQjOnjZr4igNse"
consumer_key = "8AyMTXfj10tWAv58dzQuTnVF9"
consumer_secret = "y2dtTnAUU0WzPa8YjXIRAW1pVwr11NIY1EqZERb25lXqP3KmjW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def tweet_data(keywords):
	f = codecs.open("tweet.txt",'w','utf-8')
	for word in keywords:
		public_tweets = api.search(q = word,count = 100)
		for tweet in public_tweets:
			# get rid of urls
			tweet.text = re.sub('\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet.text, flags=re.MULTILINE)
			#f.write("user: " + tweet.user.screen_name + " text: " + tweet.text + " time: " + str(tweet.created_at) + ",\n" )
			f.write(tweet.text + ",\n")
	f.close()


# to be called after tweet_data
def countFrequency():
	table = string.maketrans("","")
	f = open("tweet.txt","r")
	c = Counter()
	for line in f:
		line.translate(table, string.punctuation)
		c = Counter(line.split())
		print c['NDP']

