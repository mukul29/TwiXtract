from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import API
import os
import json

import py.twitter_credentials

import sys

class TwitterClient:
	def __init__(self, file_path, twitter_user=None):
		self.auth = TwitterAuthenticator().twitter_authenticate()
		self.twitterClient = API(self.auth)
		self.twitter_user = twitter_user
		self.file_path = file_path
		try:
			os.remove(self.file_path)
		except:
			pass

	def get_user_timeline_tweets(self, num_tweets):
		with open(self.file_path, 'a', newline='\n') as file:	
			counter = 0
			for tweet in Cursor(self.twitterClient.user_timeline, id=self.twitter_user).items(num_tweets):
				counter += 1
				print("(" + str(counter) + "/" + str(num_tweets) + ")")
				file.write(json.dumps(tweet._json))
				file.write('\n')
class TwitterAuthenticator:
	def twitter_authenticate(self):
		auth = OAuthHandler(py.twitter_credentials.CONSUMER_KEY, py.twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(py.twitter_credentials.ACCESS_TOKEN, py.twitter_credentials.ACCESS_TOKEN_SECRET)
		return auth

if __name__ == '__main__':
	
#	tweets_filename = "tweets.json"
#	hashtags = ['fifa', 'messi', 'ronaldo', 'fifawc', 'world cup']
#	myTwitterStreamer = TwitterStreamer()
#	myTwitterStreamer.stream_tweets(tweets_filename, hashtags, 5)
	
	twitterClient = TwitterClient('evilhag')
	twitterClient.get_user_timeline_tweets(10)
