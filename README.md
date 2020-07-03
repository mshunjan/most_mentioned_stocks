# Stock Hype Tracker

## Concept Summary

It is a desktop based webscraper for subreddits on Reddit.com, using the PRAW api, to extract high-volume stock tickers for the purposes
of tracking stock surges. 

### First Phase of development

It will initially start off as a command-line-interface, which will take user input. It will return, based on the user inputed values, a formatted table of the top n stock mentions in both comments and submissions, for a given period.


### Second Phase of development

Adding a gui, so it is interactive and ui accessible. Once the project is complete, consider adding livestream updates of volumes. Stock info should be displayed next to tickers.

Parameters need to be tweaked, but currently, it is conceptualized to return the top 5 tickers, in accordance 
to those parameters. It should also be able to decide which subreddit to scrape from, and multiple as well, though this will be a later 
implementation. Note that I have switched to PushSift since there was no way to
track time other than by post, rather than by date.

Requirements

- Python
- PushShift API
- PyQT5 