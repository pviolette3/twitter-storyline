import twython
import json

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
    main()