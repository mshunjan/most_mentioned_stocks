import praw
import datetime  

class Submissions():
    ''' A class to represent a submissions instance for a given subreddit. '''

    def __init__(self, subred):
        ''' Initializes the submissions instance '''
        ## creates a subreddit attribute based on the given string
        self.subred = reddit.subreddit(subred)  

    @staticmethod
    def get_date(submission):
        time = submission.created
        return datetime.datetime.fromtimestamp(time)

    def retrieve_submission(self, section, submission):
        ''' Retrieves the title for the submission ''' 
        self.section = section 
        if self.section == 'title':
            return submission.title
        else:
            return submission.selftext

    def live_submissions(self):
        ''' Retrieves titles for live submissions '''
        for submission in self.subred.stream.submissions():
            print(submission.title)
  
        
reddit = praw.Reddit(client_id="id",
                     client_secret="secret",
                     user_agent="my user agent")