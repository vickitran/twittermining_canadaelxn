# twittermining_canadaelxn
A simple python app that text mines twitter data related to the Canada Federal Election 2015. It determines the frequency that each significant party in Canada (NDP, Liberal, Conservative) is mentioned in a select batch of tweets and visualises it through a plot.

To further analyse the data, it was assumed that a positive tweet for a party correlates to the user voting for this party. Only tweets in which the confidence of the classifier was above 80% was taken into consideration (which correlates to human sentiment). 

# To Use
Run main.py to create plot of party frequencies in tweets

To look at current streaming sentiment, enter into your python environment:
python streamSentiment.py &
python plotSentiment.py &

# Conclusion
In comparision to the official CBC polls, the sentiment plot produces a general pattern that loosely aligns with the polls. The application can determine the current sentiment of users, especially during active times such as a debate or political campaigning event. As a result, Twitter can be used as a valuable resource to determine the current opinions of Canadians on the different parties and the effects on the outcome of the upcoming election.

# Shortcomings and Future Requirements
The application currently only looks at the English tweets which disregards the large Francophone population of Canada. The application was unable to locate tweets specifically to Canada and has to rely on relevant hashtags and labels to narrow down tweet results and avoid noise from US elections. Therefore, tweets need to be restricted and analysed at the federal, provincial, and municipal level. The sentiment of the tweets should be analysed at a deeper level by seperating sentiment values to labels such as highly positive, neutral, somewhat positive/negative. A training and testing set for the classifiers that is more relevant towards Canadian elections needs to used.  Different assumptions must also be analysed carefully such as if the user base of Twitter is centric towards one party over another. The application can only look at recent data - historical data would provide much more insight and prediction of results.
