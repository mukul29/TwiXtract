import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
from textblob import TextBlob
from matplotlib import style
import re
import random
import webbrowser

import py.languages

# # # Setting the style for the plot # # #
style.use('ggplot')

class PresentLiveData:
	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename
		self.tweets_list = []
		self.tweets_converted_list = []
		self.count_positive_sentiment = 0
		self.count_neutral_sentiment = 0
		self.count_negative_sentiment = 0
		self.tweets_length_list = []
		self.web_user_count = 0
		self.android_user_count = 0
		self.iphone_user_count = 0
		self.others_user_count = 0
		self.df = pd.DataFrame()

	def clear_data(self):
		self.tweets_list = []
		self.tweets_converted_list = []
		self.count_positive_sentiment = 0
		self.count_neutral_sentiment = 0
		self.count_negative_sentiment = 0
		self.tweets_length_list = []
		self.web_user_count = 0
		self.android_user_count = 0
		self.iphone_user_count = 0
		self.others_user_count = 0
		self.df = pd.DataFrame()


	def make_tweets_list(self):
		for line in open(self.fetched_tweets_filename):
			try:
				self.tweets_list.append(line)
			except:
				continue

	def make_dataframe(self):
		for tweet_json in self.tweets_list:
			try:
				tweet_dict = json.loads(tweet_json)
				tweet_converted_dict = {
						'id': tweet_dict['id'],
						'date': tweet_dict['created_at'],
						'username': tweet_dict['user']['screen_name'],
						'text': tweet_dict['text'],
						'lang': tweet_dict['lang']
					}
				try:
					tweet_converted_dict['retweet_count'] = int(tweet_dict['retweeted_status']['retweet_count'])
				except KeyError:
					tweet_converted_dict['retweet_count'] = 0
				
				"""	
				Keeping count of no of users using each platform to post tweets
				"""
				tweet_source = tweet_dict['source']
	
				if re.search('web', tweet_source, re.IGNORECASE):
					self.web_user_count += 1
					tweet_converted_dict['source'] = 'web'
	
				elif re.search('android', tweet_source, re.IGNORECASE):
					self.android_user_count += 1
					tweet_converted_dict['source'] = 'android'
	
				elif re.search('iphone', tweet_source, re.IGNORECASE):
					self.iphone_user_count += 1
					tweet_converted_dict['source'] = 'iphone'
	
				else:
					tweet_converted_dict['source'] = 'others'
					self.others_user_count += 1
	
				"""
				Finding the sentiment value and determining whether its positive, negative or neutral
				"""
				
				if tweet_dict['lang'] == 'en':
					tweet_sentiment_value = TextBlob(tweet_dict['text']).sentiment.polarity
					tweet_converted_dict['sentiment_value'] = tweet_sentiment_value
					if tweet_sentiment_value > 0:
						tweet_converted_dict['sentiment'] = 'Positive'
						self.count_positive_sentiment += 1
					elif tweet_sentiment_value == 0:
						tweet_converted_dict['sentiment'] = 'Neutral'
						self.count_neutral_sentiment += 1
					else:
						tweet_converted_dict['sentiment'] = 'Negative'
						self.count_negative_sentiment += 1
				else:
					tweet_sentiment_value = None
					tweet_converted_dict['sentiment_value'] = None
					tweet_converted_dict['sentiment'] = None
	
				self.tweets_converted_list.append(tweet_converted_dict)
			except KeyError:
				print("Getting rate limited")
				continue
		
		# # # Making the dataframe # # #
		self.df = pd.DataFrame(self.tweets_converted_list)
		self.df.set_index('id', inplace = True)

	def show_dataframe(self):
		#print(self.df)
		html_file_path = 'temp/tweets.html'
		self.df.to_html(html_file_path)
		webbrowser.open(html_file_path)

	def dataframe_to_csv(self, file_name):

		self.df.to_csv(file_name)

	def retweets_sentiment_scatter(self):
		number_of_rows = len(self.df)
		plt.scatter(self.df.sentiment_value, self.df.retweet_count, c=np.random.rand(number_of_rows), s=10)
		plt.ylabel('Number of Retweets', fontsize=15)
		plt.xlabel('Sentiment Value', fontsize=15)
		plt.title('Scatter Plot', fontsize=15, fontweight='medium')
		plt.show()
	
	def sentiment_pie(self):
		slices_nature = [self.count_positive_sentiment, self.count_neutral_sentiment, self.count_negative_sentiment]
		activities_nature = ['Positive', 'Neutral', 'Negative']
		explode = [0, 0, 0.1]
		col = ['g', 'y', 'darkred']
		plt.pie(slices_nature, labels=activities_nature, explode=explode, shadow=True, colors=col, autopct='%1.1f%%', startangle=90)
		plt.axis('equal')
		plt.title('Tweets Nature')
#		plt.legend()
		plt.show()

	def source_bar(self):
		tweets_by_source = self.df['source'].value_counts()
		
		fig, ax = plt.subplots()
		ax.tick_params(axis='x', labelsize=10)
		ax.tick_params(axis='y', labelsize=10)
		ax.set_xlabel('Number of Tweets', fontsize=10)
		ax.set_ylabel('Sources', fontsize=10)
		ax.set_title('Top Sources', fontsize=10, fontweight='medium')

		tweets_by_source[:4].plot(ax=ax, kind='barh', color=['b', 'g', 'r', 'y'])
		plt.show()

	def language_bar(self):
		tweets_by_lang = self.df['lang'].value_counts()
		lang_dict = tweets_by_lang[:5].to_dict()
		lang_keys = list(lang_dict.keys())
		lang_full_keys = []
		for key in lang_keys:
			try:
				lang_full_keys.append(py.languages.languages_dict[key])
			except:
				lang_full_keys.append('Others')
		print(lang_full_keys)
		lang_values = list(lang_dict.values())
		print(lang_values)

		color = ['darkred', 'g', 'teal', 'y', 'violet']
		plt.ylabel('Number of Tweets', fontsize=15)
		plt.xlabel('Languages', fontsize=15)
		plt.title('Top Languages', fontsize=15, fontweight='medium')
		plt.bar(lang_full_keys, lang_values, align='center', color=color)
		plt.show()

if __name__ == '__main__':
	fetched_tweets_filename = 'tweets.json'
	presentLiveData = PresentLiveData(fetched_tweets_filename)
	presentLiveData.make_tweets_list()
	presentLiveData.make_dataframe()
	presentLiveData.show_dataframe()
	presentLiveData.retweets_sentiment_scatter()
	presentLiveData.sentiment_pie()
	presentLiveData.source_bar()
	presentLiveData.language_bar()
