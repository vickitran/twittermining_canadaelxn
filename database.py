import MySQLdb

# connect to database    server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("localhost","root","cookies","root$tutorial")

# cursor used to execute queries
c = conn.cursor()

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]

        # execute specified query: 
        c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))

        return True

    def on_error(self, status):
        print status