from collections import namedtuple
import json
from dbco import * # this imports the db connexion

Tweet = namedtuple('Tweet', ['guid', 'text', 'author', 'timestamp'])
class Tweet(namedtuple('Tweet', ['guid', 'text', 'author', 'timestamp'])):
    def __new__(cls, guid='', text='', author='', timestamp=0):
        return super(Tweet, cls).__new__(cls, guid, text, author, timestamp)

def saveNewTweets(newTweets):
	Ts = []
	for t in newTweets:
		if isValid(t):
			Ts.append(t._asdict())
		else:
			print "Article from source: ", a.source, "feed: ", a.feed, " was invalid"
	if len(Ts) > 0:
		insertArticles(Ts)

def insertArticles(Ts):
	for t in Ts:
		db.tweet.update({'guid': t['guid']}, {'$set': t}, upsert=True) # if the GUID is already in the set

def saveNewArticlesFile(newArticles):
	with open("DB_ex.txt", "a") as f:
		for a in newArticles:
			if isValid(a):
				f.write(json.dumps(a._asdict())+'\n')
			else:
				print "Article from source: ", a.source, "feed: ", a.feed, " was invalid"

def isValid(t):
	if t.guid == '':
		return False
	if t.text == '':
		return False
	if t.author == '':
		return False
	if t.timestamp < 500:
		return False
	return True


tw = Tweet('blala', 'hello my tweet', 'phili', 234567567)

saveNewTweets([tw])