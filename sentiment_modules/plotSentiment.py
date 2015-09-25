'''
plotSentiment.py
21 Sep 2015 | Tonny and Vicki

Plots the Twitter sentiment of the parties
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use('ggplot')

fig = plt.figure(figsize=(10,6))
fig.suptitle('Party Twitter Sentiment Analysis', fontsize=18)
ax1 = fig.add_subplot(1,1,1)
fig.text(0.5, 0.02, 'Time', ha='center', va='center')
fig.text(0.06, 0.5, 'Tweet Sentiment', ha='center', va='center', rotation='vertical')

def animate(i):
	pullDataNDP = open('twitter-NDP.txt', 'r').read()
	pullDataLiberal = open('twitter-liberal.txt', 'r').read()
	pullDataConservative = open('twitter-conservative.txt', 'r').read()
	linesNDP = pullDataNDP.split('\n')
	linesLiberal = pullDataLiberal.split('\n')
	linesConservative = pullDataConservative.split('\n')

	xarNDP = []
	xarLiberal = []
	xarConservative = []

	yarNDP = []
	yarLiberal = []
	yarConservative = []

	xNDP = 0
	xLiberal = 0
	xConservative = 0
	yNDP = 0
	yLiberal = 0
	yConservative = 0

	for a,b,c in zip(linesNDP[-200:], linesLiberal[-200:], linesConservative[-200:]):
		xNDP += 1
		xLiberal += 1
		xConservative += 1
		if "pos" in a:
			yNDP += 1
		elif "neg" in a:
			yNDP -= 1
		if "pos" in b:
			yLiberal += 1
		elif "neg" in b:
			yLiberal -= 1
		if "pos" in c:
			yConservative += 1
		elif "neg" in c:
			yConservative -= 1

		xarNDP.append(xNDP)
		yarNDP.append(yNDP)
		xarLiberal.append(xLiberal)
		yarLiberal.append(yLiberal)
		xarConservative.append(xConservative)
		yarConservative.append(yConservative)

	ax1.clear()
	ax1.plot(xarNDP, yarNDP, label='NDP', color='orange')
	ax1.plot(xarLiberal, yarLiberal, label='Liberal', color='red')
	ax1.plot(xarConservative, yarConservative, label='Conservative', color='blue')
	# Place a legend to the right of this smaller figure.
	ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title='Party')
ani = animation.FuncAnimation(fig, animate, interval=1000)


plt.subplots_adjust(top=.9, bottom=.1, hspace=.1, left=.1, right=.75, wspace=.1)
plt.show()