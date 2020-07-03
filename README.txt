Quick Start:

$ python3 stock_tracker.py

Notes:

This is meant to be a test project for the concept layed out in the concept summary. Originally, this was to be the only project for this concept, but I realized that the API implemented in this program had deprecated some functionality I wanted for my app. As such, I will be remaking this app, as an executable with a more useful API, and implementing some larger features.

Concept Summary

It is a desktop based webscraper for subreddits on Reddit.com, using the PRAW api, to extract high-volume stock tickers for the purposes of tracking stock surges. It will initially start off as a command-line-interface, then progress to a gui format, initially interactive, and then finally a widget. Parameters need to be tweaked, but currently, it is conceptualized to return the top 5 tickers, in accordance to those parameters. It should also be able to decide which subreddit to scrape from, and multiple as well, though this will be a later 
implementation. 

Requirements

- Python
- Reddit account to get PRAW
- PRAW
- Client ID and client secret 
- User agent



