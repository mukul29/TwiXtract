# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxLiveTweets = QtWidgets.QGroupBox(self.tab)
        self.groupBoxLiveTweets.setObjectName("groupBoxLiveTweets")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxLiveTweets)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelHashtags = QtWidgets.QLabel(self.groupBoxLiveTweets)
        self.labelHashtags.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelHashtags.setFont(font)
        self.labelHashtags.setObjectName("labelHashtags")
        self.gridLayout_3.addWidget(self.labelHashtags, 0, 0, 1, 1)
        self.lineEditLiveHashtags = QtWidgets.QLineEdit(self.groupBoxLiveTweets)
        self.lineEditLiveHashtags.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditLiveHashtags.setText("")
        self.lineEditLiveHashtags.setObjectName("lineEditLiveHashtags")
        self.gridLayout_3.addWidget(self.lineEditLiveHashtags, 0, 1, 1, 1)
        self.labelLiveStreamStatus = QtWidgets.QLabel(self.groupBoxLiveTweets)
        self.labelLiveStreamStatus.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLiveStreamStatus.setFont(font)
        self.labelLiveStreamStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLiveStreamStatus.setObjectName("labelLiveStreamStatus")
        self.gridLayout_3.addWidget(self.labelLiveStreamStatus, 2, 1, 1, 1)
        self.lineEditLiveNumTweets = QtWidgets.QLineEdit(self.groupBoxLiveTweets)
        self.lineEditLiveNumTweets.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditLiveNumTweets.setObjectName("lineEditLiveNumTweets")
        self.gridLayout_3.addWidget(self.lineEditLiveNumTweets, 1, 1, 1, 1)
        self.pushButtonLiveStream = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonLiveStream.setFont(font)
        self.pushButtonLiveStream.setObjectName("pushButtonLiveStream")
        self.gridLayout_3.addWidget(self.pushButtonLiveStream, 2, 0, 1, 1)
        self.pushButtonLiveShowDataframe = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButtonLiveShowDataframe.setFont(font)
        self.pushButtonLiveShowDataframe.setObjectName("pushButtonLiveShowDataframe")
        self.gridLayout_3.addWidget(self.pushButtonLiveShowDataframe, 5, 0, 1, 2)
        self.labelLiveTweetsNumber = QtWidgets.QLabel(self.groupBoxLiveTweets)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelLiveTweetsNumber.setFont(font)
        self.labelLiveTweetsNumber.setObjectName("labelLiveTweetsNumber")
        self.gridLayout_3.addWidget(self.labelLiveTweetsNumber, 1, 0, 1, 1)
        self.pushButtonLiveMakeCsv = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        self.pushButtonLiveMakeCsv.setObjectName("pushButtonLiveMakeCsv")
        self.gridLayout_3.addWidget(self.pushButtonLiveMakeCsv, 6, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLiveLanguagesBar = QtWidgets.QLabel(self.groupBoxLiveTweets)
        self.labelLiveLanguagesBar.setMaximumSize(QtCore.QSize(80, 80))
        self.labelLiveLanguagesBar.setText("")
        self.labelLiveLanguagesBar.setPixmap(QtGui.QPixmap(":/bar_logo/bar_logo.png"))
        self.labelLiveLanguagesBar.setScaledContents(True)
        self.labelLiveLanguagesBar.setObjectName("labelLiveLanguagesBar")
        self.horizontalLayout.addWidget(self.labelLiveLanguagesBar)
        self.pushButtonLiveLanguagesBar = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        self.pushButtonLiveLanguagesBar.setObjectName("pushButtonLiveLanguagesBar")
        self.horizontalLayout.addWidget(self.pushButtonLiveLanguagesBar)
        self.labelLiveSourcesBar = QtWidgets.QLabel(self.groupBoxLiveTweets)
        self.labelLiveSourcesBar.setMaximumSize(QtCore.QSize(80, 80))
        self.labelLiveSourcesBar.setText("")
        self.labelLiveSourcesBar.setPixmap(QtGui.QPixmap(":/bar_logo/bar_logo.png"))
        self.labelLiveSourcesBar.setScaledContents(True)
        self.labelLiveSourcesBar.setObjectName("labelLiveSourcesBar")
        self.horizontalLayout.addWidget(self.labelLiveSourcesBar)
        self.pushButtonLiveSourcesBar = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        self.pushButtonLiveSourcesBar.setObjectName("pushButtonLiveSourcesBar")
        self.horizontalLayout.addWidget(self.pushButtonLiveSourcesBar)
        self.gridLayout_3.addLayout(self.horizontalLayout, 7, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLiveScatter = QtWidgets.QLabel(self.groupBoxLiveTweets)
        self.labelLiveScatter.setMaximumSize(QtCore.QSize(80, 80))
        self.labelLiveScatter.setText("")
        self.labelLiveScatter.setPixmap(QtGui.QPixmap(":/scatter_logo/scatter_logo.png"))
        self.labelLiveScatter.setScaledContents(True)
        self.labelLiveScatter.setObjectName("labelLiveScatter")
        self.horizontalLayout_2.addWidget(self.labelLiveScatter)
        self.pushButtonLiveScatter = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        self.pushButtonLiveScatter.setObjectName("pushButtonLiveScatter")
        self.horizontalLayout_2.addWidget(self.pushButtonLiveScatter)
        self.labelLiveSentimentPie = QtWidgets.QLabel(self.groupBoxLiveTweets)
        self.labelLiveSentimentPie.setMaximumSize(QtCore.QSize(80, 80))
        self.labelLiveSentimentPie.setText("")
        self.labelLiveSentimentPie.setPixmap(QtGui.QPixmap(":/pie_logo/pie_logo.svg"))
        self.labelLiveSentimentPie.setScaledContents(True)
        self.labelLiveSentimentPie.setObjectName("labelLiveSentimentPie")
        self.horizontalLayout_2.addWidget(self.labelLiveSentimentPie)
        self.pushButtonLiveSentimentPie = QtWidgets.QPushButton(self.groupBoxLiveTweets)
        self.pushButtonLiveSentimentPie.setObjectName("pushButtonLiveSentimentPie")
        self.horizontalLayout_2.addWidget(self.pushButtonLiveSentimentPie)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 8, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBoxLiveTweets, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelUserLanguagesBar = QtWidgets.QLabel(self.tab_2)
        self.labelUserLanguagesBar.setMaximumSize(QtCore.QSize(80, 80))
        self.labelUserLanguagesBar.setText("")
        self.labelUserLanguagesBar.setPixmap(QtGui.QPixmap(":/bar_logo/bar_logo.png"))
        self.labelUserLanguagesBar.setScaledContents(True)
        self.labelUserLanguagesBar.setObjectName("labelUserLanguagesBar")
        self.horizontalLayout_3.addWidget(self.labelUserLanguagesBar)
        self.pushButtonUserLanguagesBar = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonUserLanguagesBar.setObjectName("pushButtonUserLanguagesBar")
        self.horizontalLayout_3.addWidget(self.pushButtonUserLanguagesBar)
        self.labelUserSourcesBar = QtWidgets.QLabel(self.tab_2)
        self.labelUserSourcesBar.setMaximumSize(QtCore.QSize(80, 80))
        self.labelUserSourcesBar.setText("")
        self.labelUserSourcesBar.setPixmap(QtGui.QPixmap(":/bar_logo/bar_logo.png"))
        self.labelUserSourcesBar.setScaledContents(True)
        self.labelUserSourcesBar.setObjectName("labelUserSourcesBar")
        self.horizontalLayout_3.addWidget(self.labelUserSourcesBar)
        self.pushButtonUserSourcesBar = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonUserSourcesBar.setObjectName("pushButtonUserSourcesBar")
        self.horizontalLayout_3.addWidget(self.pushButtonUserSourcesBar)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.groupBoxUserTweets = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBoxUserTweets.setFont(font)
        self.groupBoxUserTweets.setObjectName("groupBoxUserTweets")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxUserTweets)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonUserStream = QtWidgets.QPushButton(self.groupBoxUserTweets)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButtonUserStream.setFont(font)
        self.pushButtonUserStream.setObjectName("pushButtonUserStream")
        self.gridLayout_4.addWidget(self.pushButtonUserStream, 2, 0, 1, 1)
        self.labelUsername = QtWidgets.QLabel(self.groupBoxUserTweets)
        self.labelUsername.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labelUsername.setFont(font)
        self.labelUsername.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelUsername.setObjectName("labelUsername")
        self.gridLayout_4.addWidget(self.labelUsername, 0, 0, 1, 1)
        self.lineEditUsername = QtWidgets.QLineEdit(self.groupBoxUserTweets)
        self.lineEditUsername.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.gridLayout_4.addWidget(self.lineEditUsername, 0, 1, 1, 1)
        self.labelUserNumTweets = QtWidgets.QLabel(self.groupBoxUserTweets)
        self.labelUserNumTweets.setObjectName("labelUserNumTweets")
        self.gridLayout_4.addWidget(self.labelUserNumTweets, 1, 0, 1, 1)
        self.lineEditUserNumTweets = QtWidgets.QLineEdit(self.groupBoxUserTweets)
        self.lineEditUserNumTweets.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditUserNumTweets.setObjectName("lineEditUserNumTweets")
        self.gridLayout_4.addWidget(self.lineEditUserNumTweets, 1, 1, 1, 1)
        self.labelUserStreamStatus = QtWidgets.QLabel(self.groupBoxUserTweets)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelUserStreamStatus.setFont(font)
        self.labelUserStreamStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUserStreamStatus.setObjectName("labelUserStreamStatus")
        self.gridLayout_4.addWidget(self.labelUserStreamStatus, 2, 1, 1, 1)
        self.pushButtonUserMakeCsv = QtWidgets.QPushButton(self.groupBoxUserTweets)
        self.pushButtonUserMakeCsv.setObjectName("pushButtonUserMakeCsv")
        self.gridLayout_4.addWidget(self.pushButtonUserMakeCsv, 4, 0, 1, 2)
        self.pushButtonUserShowDataframe = QtWidgets.QPushButton(self.groupBoxUserTweets)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButtonUserShowDataframe.setFont(font)
        self.pushButtonUserShowDataframe.setObjectName("pushButtonUserShowDataframe")
        self.gridLayout_4.addWidget(self.pushButtonUserShowDataframe, 3, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBoxUserTweets, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelUserScatter = QtWidgets.QLabel(self.tab_2)
        self.labelUserScatter.setMaximumSize(QtCore.QSize(80, 80))
        self.labelUserScatter.setText("")
        self.labelUserScatter.setPixmap(QtGui.QPixmap(":/scatter_logo/scatter_logo.png"))
        self.labelUserScatter.setScaledContents(True)
        self.labelUserScatter.setObjectName("labelUserScatter")
        self.horizontalLayout_5.addWidget(self.labelUserScatter)
        self.pushButtonUserScatterPlot = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonUserScatterPlot.setObjectName("pushButtonUserScatterPlot")
        self.horizontalLayout_5.addWidget(self.pushButtonUserScatterPlot)
        self.labelUserSentimentPie = QtWidgets.QLabel(self.tab_2)
        self.labelUserSentimentPie.setMaximumSize(QtCore.QSize(80, 80))
        self.labelUserSentimentPie.setText("")
        self.labelUserSentimentPie.setPixmap(QtGui.QPixmap(":/pie_logo/pie_logo.svg"))
        self.labelUserSentimentPie.setScaledContents(True)
        self.labelUserSentimentPie.setObjectName("labelUserSentimentPie")
        self.horizontalLayout_5.addWidget(self.labelUserSentimentPie)
        self.pushButtonUserSentimentPie = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonUserSentimentPie.setObjectName("pushButtonUserSentimentPie")
        self.horizontalLayout_5.addWidget(self.pushButtonUserSentimentPie)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineEditLiveHashtags)
        MainWindow.setTabOrder(self.lineEditLiveHashtags, self.lineEditLiveNumTweets)
        MainWindow.setTabOrder(self.lineEditLiveNumTweets, self.pushButtonLiveStream)
        MainWindow.setTabOrder(self.pushButtonLiveStream, self.pushButtonLiveShowDataframe)
        MainWindow.setTabOrder(self.pushButtonLiveShowDataframe, self.pushButtonLiveMakeCsv)
        MainWindow.setTabOrder(self.pushButtonLiveMakeCsv, self.pushButtonLiveLanguagesBar)
        MainWindow.setTabOrder(self.pushButtonLiveLanguagesBar, self.pushButtonLiveSourcesBar)
        MainWindow.setTabOrder(self.pushButtonLiveSourcesBar, self.pushButtonLiveScatter)
        MainWindow.setTabOrder(self.pushButtonLiveScatter, self.pushButtonLiveSentimentPie)
        MainWindow.setTabOrder(self.pushButtonLiveSentimentPie, self.lineEditUsername)
        MainWindow.setTabOrder(self.lineEditUsername, self.lineEditUserNumTweets)
        MainWindow.setTabOrder(self.lineEditUserNumTweets, self.pushButtonUserStream)
        MainWindow.setTabOrder(self.pushButtonUserStream, self.pushButtonUserShowDataframe)
        MainWindow.setTabOrder(self.pushButtonUserShowDataframe, self.pushButtonUserMakeCsv)
        MainWindow.setTabOrder(self.pushButtonUserMakeCsv, self.pushButtonUserLanguagesBar)
        MainWindow.setTabOrder(self.pushButtonUserLanguagesBar, self.pushButtonUserSourcesBar)
        MainWindow.setTabOrder(self.pushButtonUserSourcesBar, self.pushButtonUserScatterPlot)
        MainWindow.setTabOrder(self.pushButtonUserScatterPlot, self.pushButtonUserSentimentPie)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TwiXtract"))
        self.groupBoxLiveTweets.setTitle(_translate("MainWindow", "Stream Live Tweets for certain Hashtags"))
        self.labelHashtags.setText(_translate("MainWindow", "Enter Hashtags (Seperated by commas):"))
        self.labelLiveStreamStatus.setText(_translate("MainWindow", "Idle"))
        self.pushButtonLiveStream.setText(_translate("MainWindow", "Start Streaming"))
        self.pushButtonLiveShowDataframe.setText(_translate("MainWindow", "Show Dataframe"))
        self.labelLiveTweetsNumber.setText(_translate("MainWindow", "Enter Number of Tweets to Fetch:"))
        self.pushButtonLiveMakeCsv.setText(_translate("MainWindow", "Save Dataframe to CSV File"))
        self.pushButtonLiveLanguagesBar.setText(_translate("MainWindow", "Top Languages Bar Chart"))
        self.pushButtonLiveSourcesBar.setText(_translate("MainWindow", "Top Sources"))
        self.pushButtonLiveScatter.setText(_translate("MainWindow", "Retweets vs. Sentiment"))
        self.pushButtonLiveSentimentPie.setText(_translate("MainWindow", "Sentiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Live Tweets"))
        self.pushButtonUserLanguagesBar.setText(_translate("MainWindow", "Top Languages Bar Chart"))
        self.pushButtonUserSourcesBar.setText(_translate("MainWindow", "Top Sources"))
        self.groupBoxUserTweets.setTitle(_translate("MainWindow", "Fetch Tweets for a Particular User"))
        self.pushButtonUserStream.setText(_translate("MainWindow", "Start Streaming"))
        self.labelUsername.setText(_translate("MainWindow", "Enter Username:"))
        self.labelUserNumTweets.setText(_translate("MainWindow", "Enter Number of Tweets to Fetch:"))
        self.labelUserStreamStatus.setText(_translate("MainWindow", "Idle"))
        self.pushButtonUserMakeCsv.setText(_translate("MainWindow", "Save Dataframe to CSV file"))
        self.pushButtonUserShowDataframe.setText(_translate("MainWindow", "Show Dataframe"))
        self.pushButtonUserScatterPlot.setText(_translate("MainWindow", "Retweets Vs. Sentiment"))
        self.pushButtonUserSentimentPie.setText(_translate("MainWindow", "Sentiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "User Tweets"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
