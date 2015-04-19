#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from twitter import *
import os
import sys
import csv
import random

MANPAGE_URL = 'http://man7.org/linux/man-pages/'
TWEETDATA = 'manpage-tweetdata/manpage-tweetdata.csv'
HASHTAGS = "#linux #manpage"
SPACES_ELIPSES = 2 + 3
TWITTER_URL_LEN = 22

def twitter_authentication():
	CONSUMER_KEYS = os.path.expanduser('.twitter-consumer-keys')
	CONSUMER_KEY, CONSUMER_SECRET = read_token_file(CONSUMER_KEYS)

	MY_TWITTER_CREDS = os.path.expanduser('.twitter-manpage-du-jour-credentials')
	if not os.path.exists(MY_TWITTER_CREDS):
		oauth_dance("manpage-du-jour", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
	twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
	
	return twitter

def grabcsvrow():
   rowindex = 0
   with open(TWEETDATA, 'rb') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      rowcount = sum(1 for row in csvreader)
      rowindex = random.randint(0, rowcount)
      csvfile.close()

   #can't easily 'reset' loop or iterator, so open file again...
   with open(TWEETDATA, 'rb') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for i,row in enumerate(csvreader):
         if i == rowindex:
            return row

def create_str(manpage_str):

   #Tweet length: 118 minus space for additional chars
   TWITTER_CHARACTER_LEN = (118 - SPACES_ELIPSES) - len(HASHTAGS)

   #Create string...
   update = manpage_str[0:TWITTER_CHARACTER_LEN].strip('.') + "... "

   #Return...
   return update

def maketweet():
   #118 characters including punctuation and hashtags + 22 characters for the URL

   #test string to maintain for future testing...
   test_str = "This is an update slightly longer than 118 characters long so that I can test my twitter update work. Will it work? Won't it? I dont know..."

   command = grabcsvrow()

   #for future testing...
   #command_str = create_str(test_str)

   command_str = create_str(command[0] + ": " + command[1])
   url = MANPAGE_URL + command[2].strip('.').strip('/')

   #command... url #hashtag
   tweet = command_str + url + " " + HASHTAGS
   return tweet

def main():
   twitter = twitter_authentication()

   # Create and output tweet...
   manpagetweet = maketweet()
   sys.stdout.write("\n" + manpagetweet + "\n\n")

   # Update twitter status
   twitter.statuses.update(status=manpagetweet)

if __name__ == "__main__":
    main()
