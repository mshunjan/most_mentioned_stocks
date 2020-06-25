import re
from submissions import Submissions
from ticker import Ticker

# r'\b[A-Z]{4}\b'
def run_tracker(): 
    ''' Runs stock tracker with Submissions and ticker instances ''' 
    subreddit = Submissions('pennystocks') 
    stock = Ticker()
    for submission in subreddit.subred.new(limit=100): 
        stock.find_ticker(subreddit.retrieve_submission('title', submission))

run_tracker()