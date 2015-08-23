<<<<<<< HEAD
import twython
import json
import requests

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
=======
import twython
import json

class TweetSampler(twython.TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print json.dumps(data)

    def on_error(self, status_code, data):
        print status_code

def main():
    with open('credentials.json') as f:
        credentials = json.load(f)
    stream = TweetSampler(
        credentials['APP_KEY'],
        credentials['APP_SECRET'],
        credentials['ACCESS_TOKEN'],
        credentials['ACCESS_TOKEN_SECRET'])
    stream.statuses.sample()

if __name__ == '__main__':
>>>>>>> f317f2a8c70e5926fa910b4c7b114f4019e00847
    main()