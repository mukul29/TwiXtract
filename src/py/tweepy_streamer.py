from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

import py.twitter_credentials

import sys

class TwitterAuthenticator:
	def twitter_authenticate(self):
		auth = OAuthHandler(py.twitter_credentials.CONSUMER_KEY, py.twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(py.twitter_credentials.ACCESS_TOKEN, py.twitter_credentials.ACCESS_TOKEN_SECRET)
		return auth

class TwitterListener(StreamListener):

	def __init__(self, fetched_tweets_filename, max_tweets):
		self.fetched_tweets_filename = fetched_tweets_filename
		self.counter = 0
		self.max_tweets = max_tweets
		try:
			os.remove(self.fetched_tweets_filename)
		except:
			pass

	def on_data(self, data):
		self.counter += 1
		if self.counter > self.max_tweets:
			return False
		print("(" + str(self.counter) + "/" + str(self.max_tweets) + ")")
		try:
			#print(data)
			with open(self.fetched_tweets_filename, "a", newline='\n') as fp:
				fp.write(data)
			return True
		except BaseException as e:
			print("Error: %s\n" % str(e))
			return False

	def on_error(self, status):
		if status == 420:
			return False
		print(status)

class TwitterStreamer:
	def __init__(self):
		self.twitterAuthenticator = TwitterAuthenticator()
		
	def stream_tweets(self, fetched_tweets_filename, hashtag_list, max_tweets):
		listener = TwitterListener(fetched_tweets_filename, max_tweets)
		auth = self.twitterAuthenticator.twitter_authenticate()

		myStream = Stream(auth, listener)
		myStream.filter(track = hashtag_list)

if __name__ == '__main__':
	
	tweets_filename = "tweets.json"
	hashtags = ['fifa', 'messi', 'ronaldo', 'fifawc', 'world cup']
	myTwitterStreamer = TwitterStreamer()
	try:
		myTwitterStreamer.stream_tweets(tweets_filename, hashtags, 5)
	except:
		print("Connection Error")
	
	#twitterClient = TwitterClient('evilhag')
	#print(twitterClient.get_user_timeline_tweets(1))
