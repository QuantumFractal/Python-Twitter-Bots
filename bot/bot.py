'''
    Twitter Bot Skeleton + Recipes
    Use this to get started making your very own Rad Twitter Bot
'''

#Import the Twitter API 
import twitter
from secrets import keys


def main():
    pass

def verifyCredentials():
    '''
        Method to verify that your keys work
        Also known as a "network connectivity test"
    '''
    print api.VerifyCredentials()


'''
    A few recipes to help you get started
    Feel free to use and edit these as you please. 
    The print statements are for your feedback only, so feel free to remove those, too. 
'''
def postStatus(status): 
    '''
        Method to post a status
        Deletes any duplicates 
        Parameters: 
            status - given status to post to Twitter 
        Returns: 
            The result of the PostUpdate API call. 
    '''
    feed = api.GetUserTimeline()
    for tweet in feed: 
        if status == tweet.text: 
            api.DestroyStatus(tweet.id)
    print "Tweeting!"
    return api.PostUpdate(status, None)


def favoriteTweet(given_tweet): 
    '''
        Method to favorite a tweet. 
        Status.GetFavorited() was not working as intended- so I just threw it into a try/except block 
        so the bot won't throw any errors when trying to favorite something 
    '''
    try: 
        api.CreateFavorite(given_tweet)
    except twitter.TwitterError, t: 
        print "You've already favorited that tweet!"

def retweetTweet(tweet_id): 
    '''
        Method to retweet a tweet. 
    '''
    try: 
        api.PostRetweet(tweet_id)
    except twitter.TwitterError, t: 
        print "You've already retweeted that tweet!"

def deleteTweet(word): 
    '''
        Method to delete a tweet with a specific word. 
        This method will ignore the case of the word. 
        Parameters: 
            word - the word to be deleted 
    '''
    word = word.lower()
    print "Looking for " + "\'" + word + "\'" + "!"
    feed = api.GetUserTimeline()
    for tweet in feed: 
        if word in tweet.text.lower(): 
            print "deleting tweet..."
            api.DestroyStatus(tweet.id)
        else: 
            print "word not found!"

def followAccount(user): 
    '''
        Follow an account
    '''
    api.CreateFriendship(user) 

def autoFavoriteMentions(): 
    '''
        Method to auto-favorite mentions
    '''
    mentions = api.GetMentions()
    for tweet in mentions: 
        print "@" + tweet.user.screen_name + " tweeted " + "\"" + tweet.text.encode('utf-8') + "\"" 
        favoriteTweet(tweet)

def searchByTerm(term): 
    '''
        Method to search for a term
    '''
    search_feed = api.GetSearch(term)
    for tweet in search_feed: 
        #use .encode() to avoid some unicode issues when trying to print tweets
        print "@" + tweet.user.screen_name.encode('utf-8') + " tweeted " + "\"" + tweet.text.encode('utf-8') + "\"" 

        #Do whatever you want here! 
        #favorite that tweet 
        #favoriteTweet(tweet)
        #follow the account that tweeted the message
        #followAccount(tweet.user.id)
        #retweet tweet 
        #retweetTweet(tweet.id)

def printTimeline(): 
    '''
        Method to print a timeline
    '''
    timeline = api.GetHomeTimeline()
    for tweet in timeline: 
        print tweet.text.encode('utf-8')

'''
    Setup
'''
api = twitter.Api(keys['consumer_key'], keys['consumer_secret'],
                  keys['client_token'], keys['client_secret'])

verifyCredentials()
#postStatus("Twitter Bot test!")
#deleteTweet('retweet me!')
#searchByTerm("#GHC15")
#autoFavoriteMentions() 
#printTimeline()
#picture = "path/to/media"
#api.PostMedia("A tweet", picture)


if __name__ == '__main__':
    main()