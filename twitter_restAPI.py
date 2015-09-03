import tweepy 
import codecs # have to encode text before writing to file

# tonny's credentials
access_token = "21627027-w4cJ0ugNNFIXzyt3YOj3In2YumXpk28a4K9RszLte"
access_token_secret = "C1kbLxrjjss8M73Dd1CUa8MgUFev2xieQjOnjZr4igNse"
consumer_key = "8AyMTXfj10tWAv58dzQuTnVF9"
consumer_secret = "y2dtTnAUU0WzPa8YjXIRAW1pVwr11NIY1EqZERb25lXqP3KmjW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = codecs.open("tweet.txt",'w','utf-8')

keywords = ['cdnpoli','elxn42']
#public_tweets = api.user_timeline("pmharper",count = 5)
for party in keywords:
	public_tweets = api.search(party, rpp = 10) 
	# rpp = The number of tweets to return per page, up to a max of 100 pages
	for tweet in public_tweets:
   		tweets.write(tweet.text + ",\n")

tweets.close()