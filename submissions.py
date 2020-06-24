import praw
 

class Submissions():
    ''' A class to represent a submissions instance for a given subreddit. '''

    def __init__(self, subred):
        ''' Initializes the submissions instance '''
        self.subred = reddit.subreddit(subred) 
 
    def retrieve_submission_text(self):
        ''' Retrieves the contents for the submission '''
        for submission in self.subred.stream.submissions():
            print(submission.title)
                
    def retrieve_submission_title(self):
        ''' Retrieves the title for the submission '''
        for submission in self.subred.stream.submissions():
            print(submission.title)
        
reddit = praw.Reddit(client_id="58vJL3gF6-Z8bg",
                    client_secret="nxAkxIeEJl8_f32TxA0fiwnVdsk",
                    user_agent="my user agent")

pennystocks = Submissions('pennystocks')

pennystocks.retrieve_submission_title()  