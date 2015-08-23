from dbco import *

tw = db.tweet.find()

for t in tw:
	print t['text']
