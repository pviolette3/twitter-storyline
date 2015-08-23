import twython
import json
import requests
from tweet import *

def main():
    with open('credentials.json') as f:
        credentials = json.load(f)
    twitter = twython.Twython(
        credentials['APP_KEY'],
        credentials['APP_SECRET'],
        credentials['ACCESS_TOKEN'],
        credentials['ACCESS_TOKEN_SECRET'])
    twitter.verify_credentials()

if __name__ == '__main__':
    import twython
    import json

class TweetSampler(twython.TwythonStreamer):
    def on_success(self, data):
        if 'text' in data and 'id_str' in data and 'user' in data and 'id_str' in data['user'] and 'timestamp_ms' in data and 'place' in data and 'id' in data['place']:
            time = int(float(data['timestamp_ms'])/1000.0)
            t = Tweet(data['id_str'], data['text'], data['user']['id_str'], time, data['place']['id'])
            saveNewTweets([t])
            print "Yay"
            # print json.dumps(data)


    def on_error(self, status_code, data):
        print status_code

ATL_BOUNDING_BOX = {
    "coordinates": [
    [
      [
        -85.605166,
        30.355644
      ],
      [
        -85.605166,
        35.000771
      ],
      [
        -80.742567,
        35.000771
      ],
      [
        -80.742567,
        30.355644
      ],
      [
        -85.605166,
        30.355644
      ]
    ]
]}

ATL_BOUNDING_BOX_CORNERS = '-85.605166,30.355644,-80.742567,35.000771'

def main():
    with open('credentials.json') as f:
        credentials = json.load(f)
    stream = TweetSampler(
        credentials['APP_KEY'],
        credentials['APP_SECRET'],
        credentials['ACCESS_TOKEN'],
        credentials['ACCESS_TOKEN_SECRET'])
    stream.statuses.filter(locations=ATL_BOUNDING_BOX_CORNERS)

if __name__ == '__main__':
    main()