import os
import json

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

##BOT KEYS
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

setTerms = ['veterans', 'suicide', 'help', 'pain', 'hopeless','nightmare']

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

class StdOutListener(StreamListener):

    #This function gets called every time a new tweet is received on the stream
    def on_data(self, data):
        #Just write data to one line in the file
        fhOut.write(data)

        #Convert the data to a json object (shouldn't do this in production; might slow down and miss tweets)
        j=json.loads(data)

        #See Twitter reference for what fields are included -- https://dev.twitter.com/docs/platform-objects/tweets
#        text=j["text"] #The text of the tweet
        user = (j['user']['screen_name'])
        text = (j['text']) #Print it out
        
        print(user, text)
        print('\n')
        
        ##MACHINE LEARNING ALGORIITHM TO DETERMINE IF SOMEONE NEEDS HELP##
        #IF TRUE:
        #tweet_helpline(user) ##For Later will spam
        #tweet_friendConnector(user) ##For Later will spam
        
    def on_error(self, status):
        print("ERROR")
        print(status)


if __name__ == '__main__':
    try:
        #Create a file to store output. "a" means append (add on to previous file)
        fhOut = open("tweets.json","a")

        #Create the listener
        l = StdOutListener()

        #Connect to the Twitter stream
        stream = Stream(auth, l,timeout=30)

        #Terms to track
        stream.filter(track=setTerms)

        #Alternatively, location box  for geotagged tweets
        #stream.filter(locations=[-0.530, 51.322, 0.231, 51.707])

    except KeyboardInterrupt:
        #User pressed ctrl+c -- get ready to exit the program
        pass
    
    #Close the
    fhOut.close()