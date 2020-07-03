import re
from submissions import Submissions
from ticker import Ticker
from collections import Counter

count = Counter()
# r'\b[A-Z]{4}\b'
def run_tracker(): 
    ''' Runs stock tracker with Submissions and ticker instances ''' 
    subreddit = Submissions('pennystocks') 
    stock = Ticker()
    for submission in subreddit.subred.new(limit=1000): 
        stock_iter = stock.find_ticker(subreddit.retrieve_submission('title', submission))
        if stock_iter != False:
            count[stock_iter] += 1
        else:
            continue 
    
    print ('Most common:')
    for company, cnt in count.most_common(5):
        print ('%s: %7d' % (company,cnt))
run_tracker()