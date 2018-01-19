"""A python twitter bot that tweets VC funding information."""


import os
import tweepy
import time
import requests
from bs4 import BeautifulSoup


HEADLINES = set()

page = requests.get("http://www.vcnewsdaily.com/")

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', '')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', '')
ACCESS_KEY = os.environ.get('ACCESS_KEY', '')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET', '')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    soup = BeautifulSoup(page.content, 'html.parser')
    headline_a_tags = soup.find_all("a", {"class": "titleLink"})
    for headline_a_tag in headline_a_tags:
        if headline_a_tag.text not in HEADLINES:
            HEADLINES.add(headline_a_tag.text)
            api.update_status(headline_a_tag.text)
            time.sleep(600)

    time.sleep(1800)
