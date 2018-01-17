"""A python twitter bot that tweets VC funding information."""


import os
import tweepy
import time
import sys

test_file = str(sys.argv[1])

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', '')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', '')
ACCESS_KEY = os.environ.get('ACCESS_KEY', '')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET', '')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(test_file, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)
