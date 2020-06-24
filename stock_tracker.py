import praw
import re

## When posting this to github, remember to blank the client_id and secret
## Initializes the reddit instance with users OAuth authentication
reddit = praw.Reddit(client_id="58vJL3gF6-Z8bg",
                     client_secret="nxAkxIeEJl8_f32TxA0fiwnVdsk",
                     user_agent="my user agent")
 
ticker = r'\b[A-Z]{4}\b'
ticker_object = re.compile(ticker)

subreddit = reddit.subreddit("pennystocks") 
for submission in subreddit.stream.submissions():
    stock = ticker_object.search(submission.title)
    if stock != None:
        print(stock.group())