import twython
import json

class TweetSampler(twython.TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print json.dumps(data)

    def on_error(self, status_code, data):
        print status_code

ATL_BOUNDING_BOX_CORNERS = '-84.7125826,33.325678,-83.3886814,33.9637709'

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