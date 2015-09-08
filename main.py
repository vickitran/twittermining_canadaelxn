import twitter_restAPI
import numpy as np
import matplotlib.pyplot as plt

keywords = ['NDP','%23cdnpoli']

# make API request (only needs to be done once)
twitter_restAPI.tweet_data(keywords)

# count word frequencies 
#twitter_restAPI.countFrequency()


# plot data
plt.style.use('ggplot')
# various labels + data
x = (1,2,3)
# polling data 
y = (40,22,22)

labels = ['NDP','Conservative','Liberal']
colors = ['#FF4D00','#3333CC','#DA291C']

bar_width = 0.5
plt.bar(x,y,bar_width,color=colors)

# spacing for x variables
xticks_pos = [i + 0.25 for i in x ]
plt.xticks(xticks_pos,labels,rotation = 'horizontal')
# turn off vertical gridlines
plt.grid(b = True, axis = 'none', linestyle = '-')
# extend plot space
plt.ylim([0,50])
plt.show()