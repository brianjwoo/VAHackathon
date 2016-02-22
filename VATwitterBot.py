import os
import time
import tweepy
import datetime

##BOT KEYS
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_helpline(user):
    '''
    Sends a public msg to the user to provide them information on where to get help.
    '''
    msg = "@" + user + " Hi! If you need someone to talk to, free to contact us at 1-800-273-8255"
    #msg = "@"+user + " Just Testing STuff"
    api.update_status(msg)
    api.create_friendship(user)

def tweet_friendConnector(user):
    '''
    Queries the API for a given users friend list and contacts a subset to help the individual in need.
    '''
    friends = api.friends(user)
    for f in friends:
        #print f.screen_name
        msg = "@"+f.screen_name + ". It seems that " + user + " could use someone to talk to."
        print msg
        #api.update_status(msg) ##THIS WILL SPAM PEOPLE 

def tweet_volunteer(user):
    '''
    Function for outreach where users can tweet at the bot to volunteer and the bot will take in their twitter information for future use.
    '''
    msg = "@"+user + " .Thanks for joining our cause!"
    api.update_status(msg)
    api.create_friendship(user)
    #Insert user into some database
    
def parse_status(status):
    '''
    Parse a status for author and text information after querying from a specific users timeline
    '''
    if 'help' in status.text.lower():
        tweet_helpline(status.author.screen_name)
    if 'volunteer' in status.text.lower():
        tweet_volunteer(status.author.screen_name)

last_status = None
#To query the API 
while(True):
    time.sleep(30)
    timeline = api.mentions_timeline()
    for status in timeline:
        print status.author.screen_name
        print status.text
        if status == last_status:
            break
        else:
            try:
                pass
                parse_status(status)
            except:
                pass
    last_status = timeline[0]