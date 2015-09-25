import twitter_restAPI
import numpy as np
import matplotlib.pyplot as plt
import database as db

keywords = ['NDP','%23cdnpoli','%23exln42']

# make API request (only needs to be done once)
twitter_restAPI.tweet_data(keywords)

# plot data
plt.style.use('ggplot')
# various labels + data
x1 = (1,2,3)
# polling data 
y1 = (40,22,22)
# twitter data
y2 = (db.getPercent('NDP'),db.getPercent('Conservative'),db.getPercent('Liberal'))
print db.getPercent('Conservative')

labels = ['NDP','Conservative','Liberal']
colors = ['#FF4D00','#3333CC','#DA291C']

bar_width = 0.5
plt.bar(x1,y1,bar_width,color=colors,label = "Polling Data")
plt.plot(x1,y2,'k-',label = "Twitter Dataset")
plt.plot()

# spacing for x variables
xticks_pos = [i + 0.25 for i in x1]
plt.xticks(xticks_pos,labels,rotation = 'horizontal')
# turn off vertical gridlines
plt.grid(b = True, axis = 'none', linestyle = '-')
# extend plot space
plt.ylim([0,50])
plt.show()