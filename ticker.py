import re

class Ticker():
    ''' A class to represent a single stock ticker '''

    def __init__(self, pattern=r'\b[A-Z]{4}\b', price=None):
        ''' Initializes the stock with its price '''
        self.pattern = re.compile(pattern)

    def find_ticker(self, query):
        ticker = self.pattern.search(query)
        if  ticker!= None:
            print(ticker.group())



