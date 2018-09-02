# TwiXtract
### Data Analysis on Twitter Data
TwiXtract lets you extract tweets from Twitter and applies sentiment analysis on them. It is based on Python 3.

### Setting Up
1. Install Python 3.5 or later.
2. Install the following Python packages using pip:

```
pip install matplotlib
pip install numpy
pip install PyQt5
pip install textblob
pip install tweepy
pip install pandas
pip install webbrowser
```
3. Clone this repository.

`git clone https://github.com/mukul29/TwiXtract.git`

4. Make a Twitter account if you don't have one already.

5. Go to https://apps.twitter.com and apply for a Twitter developer account.

6. Create a Twitter app and go to the Keys and Access Tokens tab. You'll require the following keys:

    **Consumer Key, Consumer Secret, Access Token and Access Token Secret**

7. After you have these keys, navigate to **TwiXtract/src/py** folder and add these keys to the **twitter_credentials.py** file.

8. Run the **main.py** file in **TwiXtract/src** directory.

`python main.py`
