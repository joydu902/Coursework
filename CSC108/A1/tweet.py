import math

# Use these constants in place of int and string literals to make your code
# easier to read, and less error prone.
# Note that we are using a shorter tweet length to make testing easier.
MAX_TWEET_LENGTH = 50
HASH = '#'


# Add your own constants here, as needed
OWLY_URL = "http://ow.ly/"
TWEET1 = 'Tweet 1'
TWEET2 = 'Tweet 2'
SAME = 'Same length'

def contains_owly_url(tweet):
    """ (str) -> bool

    Return True if and only if tweet contains a link to an ow.ly URL of the 
    form 'http://ow.ly/' .

    Assume tweet is a valid tweet.

    >>> contains_owly_url('Cook receives award: http://ow.ly/WXJFN')
    True
    >>> contains_owly_url('http://ow.ly/VGpA9 Team to transform U of T campus')
    True
    >>> contains_owly_url('Fairgrieve to play in goal http://www.nhl.com')
    False
    """
    return OWLY_URL in tweet


def is_valid_tweet(tweet):
    """ (str) -> bool
    
    Return True if and only if the length of tweet is larger or equal to 1 and 
    smaller or equal to MAX_TWEET_LENGTH.
    
    >>> is_valid_tweet('joy is such a cute girl')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet('joy is such a cute girl joy is such a cute girl haha.')
    False
    """
    return 1 <= len(tweet) <= MAX_TWEET_LENGTH


def add_hashtag(tweet, text):
    """ (str, str) -> str
    
    Return the new tweet with the hashtag included, if the new tweet created 
    by appending a space, the hash symbol, and the text to the end of the 
    original tweet is a valid tweet. Otherwise, Return the original tweet, if 
    the tweet is not valid when the hashtag were added. 
    
    Asuume the first parameter tweet is a valid tweet. 

    >>> add_hashtag('I like', 'csc108')
    'I like #csc108'
    >>> add_hashtag('Today is ', 'a sunny day')
    'Today is  #a sunny day'
    >>> add_hashtag('Today', 'a sunny day a sunny day a sunny day a sunny day')
    'Today'
    """
    result = tweet + ' ' + HASH + text
    if is_valid_tweet(result):
        return result
    else:
        return tweet
    

def contains_hashtag(tweet, hashtag):
    """ (str, str) -> bool
    
    Return True if and only if the first parameter tweet contains the second
    parameter hashtag. 
    
    Assume the first parameter tweet is a valid tweet.
    
    >>> contains_hashtag('I like #csc108', '#csc108')
    True
    >>> contains_hashtag('I like #csc108', '#csc')
    False
    >>> contains_hashtag("I like #CSC108 !", "#CSC108")
    True
    """
    if hashtag + " " in tweet:
        return True
    else:
        return tweet.index(hashtag) == len(tweet)-len(hashtag)
 
        
        
def report_longest(tweet1, tweet2):
    """ (str, str) -> str
    
    Return 'Tweet 1' if the first parameter tweet is longer than the second.
    Return 'Tweet 2' if the second parameter tweet is longer than the first.
    Return 'Same length' if the two tweets are with the same length. 
    
    Assume the two parameter tweets are valid tweets. 
    
    >>> report_longest('csc108', 'csc')
    'Tweet 1'
    >>> report_longest('108', 'csc108')
    'Tweet 2'
    >>> report_longest('csc108', 'mat224')
    'Same length'
    """
    if len(tweet1) > len(tweet2):
        return TWEET1
    elif len(tweet1) < len(tweet2):
        return TWEET2
    else:
        return SAME
    

def num_tweets_required(message):
    """ (str) -> int
    
    Return the minimum number of tweets that would be required to communicate 
    all of the message which means the message will be split up into several 
    tweets and each tweet's length is within the MAX_TWEET_LENGTH.
    
    >>> num_tweets_required('I love csc108 I love csc108 I love csc108')
    1
    >>> num_tweets_required('I love csc108 I love csc108 I love csc108 I love \
    csc108')
    2
    >>> num_tweets_required('I love csc108 I love csc108 I love csc108 I love \
    csc108 I love csc108 I love csc108 I love csc108 I love csc108 I love \
    csc108')
    3
    """
    return math.ceil(len(message) / MAX_TWEET_LENGTH)


def get_nth_tweet(message, n):
    """ (str, int) -> str
    
    If the length of message is larger than MAX_TWEET_LENGTH, it would need to 
    be split up into a sequence of tweets. Return the nth valid tweet in the 
    sequence of tweets, if all of the tweets in the sequence, except possibly
    the last tweet, would be of length MAX_TWEET_LENGTH. 
    
    Assume n is a positive integer value.
    
    >>> get_nth_tweet('csc108', 1)
    'csc108'
    >>> get_nth_tweet('csc108', 3)
    ''
    >>> get_nth_tweet('csc108csc108csc108csc108csc108csc108csc108csc108', 1)
    'csc108csc108csc108csc108csc108csc108csc108csc108'
    >>> get_nth_tweet('csc108csc108csc108csc108csc108csc108csc108csc108csA', 2)
    'A'
    """
    
    return message[(n - 1) * MAX_TWEET_LENGTH : n * MAX_TWEET_LENGTH]
