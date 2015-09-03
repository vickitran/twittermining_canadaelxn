#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "21627027-w4cJ0ugNNFIXzyt3YOj3In2YumXpk28a4K9RszLte"
access_token_secret = "C1kbLxrjjss8M73Dd1CUa8MgUFev2xieQjOnjZr4igNse"
consumer_key = "8AyMTXfj10tWAv58dzQuTnVF9"
consumer_secret = "y2dtTnAUU0WzPa8YjXIRAW1pVwr11NIY1EqZERb25lXqP3KmjW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])