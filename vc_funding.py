"""A python twitter bot that tweets VC funding information."""


import os
import tweepy
import time
import sys
import requests
from bs4 import BeautifulSoup
import csv

# if __name__ == '__main__':

def parse_page(page):
    """Parse funding info from webpage."""
    soup = BeautifulSoup(page.content, 'html.parser')
    companies = soup.find_all("a", {"class": "titleLink"})
    for company in companies:
        print(company.text)


    # job_summaries = []
    # for job in jobs:
    #     job_summaries.append(job.parent.parent.parent)

    # with open('jobs.csv', 'a') as csv_file:
    #     writer = csv.writer(csv_file)
    #     for job in job_summaries:
    #         title = job.find(class_='job-link').text
    #         company = job.find(class_='-name').text
    #         location = job.find(class_='-location').text
    #         date_posted = job.find(class_='-posted-date').text
    #         link = 'https://stackoverflow.com{}'.format(job.find(class_='job-link')['href'])
    #         writer.writerow([title, company, location, date_posted, link])


page = requests.get("http://www.vcnewsdaily.com/")
parse_page(page)





# test_file = page

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', '')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', '')
ACCESS_KEY = os.environ.get('ACCESS_KEY', '')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET', '')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# filename = open(test_file, 'r')
# f = filename.readlines()
# filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)
