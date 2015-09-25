import tweepy 
import codecs # have to encode text before writing to file 
import re # regular expressions 
import string 
from collections import Counter
import database as db # tonny's database code

# tonny's credentials
access_token = "21627027-w4cJ0ugNNFIXzyt3YOj3In2YumXpk28a4K9RszLte"
access_token_secret = "C1kbLxrjjss8M73Dd1CUa8MgUFev2xieQjOnjZr4igNse"
consumer_key = "8AyMTXfj10tWAv58dzQuTnVF9"
consumer_secret = "y2dtTnAUU0WzPa8YjXIRAW1pVwr11NIY1EqZERb25lXqP3KmjW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# finding time zone
# print tweet._json['user']['time_zone']
# user, tweet, time, freqNDP, freqCons, freqLib)

def tweet_data(keywords):
	for word in keywords:
		public_tweets = api.search(q = word,count = 1500)
		for tweet in public_tweets:
			# get rid of urls
			tweet.text = re.sub('\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet.text, flags=re.MULTILINE)
			#f.write("user: " + tweet.user.screen_name + " text: " + tweet.text + " time: " + str(tweet.created_at) + ",\n" )
			db.insertRow(tweet.user.screen_name, tweet.text,str(tweet.created_at),count_frequency('NDP',tweet.text),count_frequency('Conservative',tweet.text),count_frequency('Liberal',tweet.text))
			

# to be called after tweet_data
def count_frequency(search_word, tweet_text):
	c = Counter(tweet_text.split())
	return c[search_word]



