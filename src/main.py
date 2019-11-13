# # # Importing standard packages # # #
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from qrc_py import *
import webbrowser
import re
import os
import tweepy

# # # Importing my modules # # #
from ui_py.main_window import Ui_MainWindow
from py import *

live_tweets_filepath = "temp/live_tweets.json"
user_tweets_filepath = "temp/user_tweets.json"
live_tweets_html_filepath = "temp/live_tweets.html"
user_tweets_html_filepath = "temp/user_tweets.html"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.status = 0
		
		# # # Set Window Icon # # #
		self.setWindowIcon(QtGui.QIcon('assets/images/window_logo.png'))

		# # # Handling live stream push button # # #
		self.pushButtonLiveStream.clicked.connect(self.onStartLiveStream)
		self.workerThreadLive = WorkerThreadLive()
		self.workerThreadLive.taskFinishedLive.connect(self.onFinishedLiveStream)

		# # # Handling show dataframe push button # # #
		self.presentLiveData = twitter_extract_live_data.PresentLiveData(live_tweets_filepath)
		self.pushButtonLiveShowDataframe.clicked.connect(self.live_tweets_dataframe)

		# # # Handling save to csv push button # # #
		self.pushButtonLiveMakeCsv.clicked.connect(self.live_make_csv)
		
		# # # Quit Action # # #
		self.actionQuit.triggered.connect(self.close_application)	
		
		# # # Different plots # # #
		self.pushButtonLiveLanguagesBar.clicked.connect(self.show_live_languages_bar)
		self.pushButtonLiveSourcesBar.clicked.connect(self.show_live_sources_bar)
		self.pushButtonLiveScatter.clicked.connect(self.show_live_scatter)
		self.pushButtonLiveSentimentPie.clicked.connect(self.show_live_sentiment)

		# # # # # # # # # # # # USER TWEETS # # # # # # # # # # # #
		# # # Handling user stream push button # # #	
		self.pushButtonUserStream.clicked.connect(self.onStartUserStream)
		self.workerThreadUser = WorkerThreadUser()
		self.workerThreadUser.taskFinishedUser.connect(self.onFinishedUserStream)

		# # # Save to csv push button # # #
		self.pushButtonUserMakeCsv.clicked.connect(self.user_make_csv)

		# # # Handling user show dataframe pushbutton # # #
		self.presentUserData = twitter_extract_user_data.PresentUserData(user_tweets_filepath)
		self.pushButtonUserShowDataframe.clicked.connect(self.user_tweets_dataframe)
		# # # User top Languages bar push button # # #
		self.pushButtonUserLanguagesBar.clicked.connect(self.show_user_languages_bar)
		
		# # # Top Sources # # #
		self.pushButtonUserSourcesBar.clicked.connect(self.show_user_sources_bar)
		
		# # # Scatter Plot # # #
		self.pushButtonUserScatterPlot.clicked.connect(self.show_user_scatter)

		# # # Sentiment Pie Chart # # #
		self.pushButtonUserSentimentPie.clicked.connect(self.show_user_sentiment)

	def show_user_sources_bar(self):
		self.presentUserData.source_bar()

	def show_user_scatter(self):
		self.presentUserData.retweets_sentiment_scatter()

	def show_user_languages_bar(self):
		self.presentUserData.language_bar()
	
	def show_user_sentiment(self):
		self.presentUserData.sentiment_pie()

	def user_tweets_dataframe(self):
		self.presentUserData.show_dataframe(user_tweets_html_filepath)	

	def user_make_csv(self):
		try:
			name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', ".csv", "CSV files (*.csv)")
			self.presentUserData.dataframe_to_csv(str(name[0]))
		except:
			print("Cancelled")

	def onStartUserStream(self):
		try:

			os.remove(user_tweets_filepath)
			os.remove(user_tweets_html_filepath)
		except:
			pass

		self.presentUserData.clear_data()
		self.labelUserStreamStatus.setText('Fetching tweets')
		self.workerThreadUser.start()
		self.status = 1

	def onFinishedUserStream(self):
		self.status = 0
		if self.labelUserStreamStatus.text() == "Connection Error":
			return
		elif self.labelUserStreamStatus.text() == "Invalid Username":
			return
		self.labelUserStreamStatus.setText('Tweets Fetched')
		self.presentUserData.make_tweets_list()
		self.presentUserData.make_dataframe()


	def get_user_username(self):
		username = self.lineEditUsername.text()
		username = username.strip(' ')
		username = username.replace('@', '')
		if not username:
			raise SyntaxError
		print(username)
		return username
	
	def get_user_num_tweets(self):
		num_tweets = self.lineEditUserNumTweets.text()
		num_tweets = num_tweets.strip(' ')
		num_tweets = num_tweets.replace(',', '')
		if not num_tweets:
			raise SyntaxError
		else:
			try:
				num_tweets = int(num_tweets)
				return num_tweets
			except:
				raise TypeError

	# # # Plotting Live Streams # # #
	def show_live_scatter(self):
		self.presentLiveData.retweets_sentiment_scatter()

	def show_live_languages_bar(self):
		self.presentLiveData.language_bar()
	
	def show_live_sources_bar(self):
		self.presentLiveData.source_bar()
	
	def show_live_sentiment(self):
		self.presentLiveData.sentiment_pie()
	
	def live_make_csv(self):
		try:
			name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', ".csv", "CSV files (*.csv)")
			self.presentLiveData.dataframe_to_csv(str(name[0]))
		except:
			print("Cancelled")

	def close_application(self, event):
		if self.status == 0:
			choice = QtWidgets.QMessageBox.question(self, 'Exit', 'Exit the Application', 
							QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		else:
			choice = QtWidgets.QMessageBox.question(self, 'Exit', 'Streaming Tweets. Are you sure you want to quit?', 
							QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
	
		if choice == QtWidgets.QMessageBox.Yes:
			print("Exiting")
			sys.exit()
		else:
			pass

	def closeEvent(self, event):
		if self.status == 0:
			choice = QtWidgets.QMessageBox.question(self, 'Exit', 'Exit the Application', 
							QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		else:
			choice = QtWidgets.QMessageBox.question(self, 'Exit', 'Streaming Tweets. Are you sure you want to quit?', 
							QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
	
		if choice == QtWidgets.QMessageBox.Yes:
			print("Exiting")
			event.accept()
		else:
			event.ignore() 

	def live_tweets_dataframe(self):
		self.presentLiveData.show_dataframe()

	def onStartLiveStream(self):
		try:
			os.remove(live_tweets_filepath)
			os.remove(live_tweets_html_filepath)
		except:
			pass

		self.presentLiveData.clear_data()
		self.labelLiveStreamStatus.setText('Fetching tweets')
		self.workerThreadLive.start()
		self.status = 1

	def onFinishedLiveStream(self):
		self.status = 0
		if not self.labelLiveStreamStatus.text():
			self.labelLiveStreamStatus.setText("Connection Error")
			return
		self.labelLiveStreamStatus.setText('Tweets Fetched')
		self.presentLiveData.make_tweets_list()
		self.presentLiveData.make_dataframe()

	def get_live_hashtags(self):
		hashtags = self.lineEditLiveHashtags.text()
		hashtags = hashtags.strip(', ')
		if not hashtags:
			raise SyntaxError
		hashtags = hashtags.split(',')
		print(hashtags)
		return hashtags
		
	def get_live_num_tweets(self):
		num_tweets = self.lineEditLiveNumTweets.text()
		num_tweets = num_tweets.strip(' ')
		num_tweets = num_tweets.replace(',', '')
		if not num_tweets:
			raise SyntaxError
		else:
			try:
				num_tweets = int(num_tweets)
				return num_tweets
			except:
				raise TypeError

class WorkerThreadLive(QtCore.QThread):
	taskFinishedLive = QtCore.pyqtSignal()

	def run(self):
		# # Getting hashtags from the user # #
		try:
			hashtags = window.get_live_hashtags()
		except SyntaxError:
			print("Empty hashtag list")
			return

		# # Getting the number of tweets # #
		try:
			num_tweets = window.get_live_num_tweets()
		except SyntaxError:
			print("Number of tweets not entered")
			return
		except TypeError:
			print("Not a valid number")
			return

		twitterStreamer = tweepy_streamer.TwitterStreamer()
		try:
			twitterStreamer.stream_tweets(live_tweets_filepath, hashtags, num_tweets)
		except:
			print("Connection Error")
			window.status = 0
			window.labelLiveStreamStatus.setText("")
		self.taskFinishedLive.emit()

class WorkerThreadUser(QtCore.QThread):
	taskFinishedUser = QtCore.pyqtSignal()
	def run(self):
		# # Getting hashtags from the user # #
		try:
			username = window.get_user_username()
		except SyntaxError:
			print("Empty username")
			return

		# # Getting the number of tweets # #
		try:
			num_tweets = window.get_user_num_tweets()
		except SyntaxError:
			print("Number of tweets not entered")
			return
		except TypeError:
			print("Not a valid number")
			return
		
		twitterClient = tweepy_client.TwitterClient(user_tweets_filepath, username)
		try:
			twitterClient.get_user_timeline_tweets(num_tweets)
		except tweepy.error.TweepError:
			print("Invalid Username")
			window.status = 0
			window.labelUserStreamStatus.setText("Invalid Username")
		except:
			print("Connection Error")
			window.status = 0
			window.labelUserStreamStatus.setText("Connection Error")
		self.taskFinishedUser.emit()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())