import builtins

# Check for use of functions print and input.

# IMPORTANT!
# If you are getting this error message here: 
# line 11, in <module>
#     our_print = print
# invalid syntax: <string>, line 11, pos 21
# Then you are using the wrong version of Python! Make sure you have Python 3!
our_print = print


def disable_print(*args):
    raise Exception("You must not call print anywhere in your code!")

def disable_input(*args):
    raise Exception("You must not call input anywhere in your code!")

builtins.print = disable_print
builtins.input = disable_input

import tweet

# Get the initial value of the constants
constant_1_before = [50]
constant_2_before = ['#']

# Type check tweet.contains_owly_url
result = tweet.contains_owly_url('Test 123')
assert isinstance(result, bool), \
       '''tweet.contains_owly_url should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.is_valid_tweet
result = tweet.is_valid_tweet('Test 123')
assert isinstance(result, bool), \
       '''tweet.is_valid_tweet should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.add_hashtag
result = tweet.add_hashtag('Test 123', 'a').strip()
assert isinstance(result, str), \
       '''tweet.add_hashtag should return a str, but returned {0}
       .'''.format(type(result))
assert result == 'Test 123 #a', \
       '''tweet.add_hashtag should return 'Test 123 #a', but returned '{0}'
       .'''.format(result)

# Type check tweet.contains_hashtag
result = tweet.contains_hashtag('Test 123', '123')
assert isinstance(result, bool), \
       '''tweet.contains_hashtag should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.report_longest
result = tweet.report_longest('Test 123', '123').strip()
assert isinstance(result, str), \
       '''tweet.report_longest should return an str, but returned {0}
       .'''.format(type(result))
assert result == 'Tweet 1', \
       '''tweet.report_longest should return 'Tweet 1', but returned {0}
       .'''.format(result)

# Type check tweet.num_tweets_required
result = tweet.num_tweets_required('Test 123')
assert isinstance(result, int), \
       '''tweet.num_tweets_required should return an int, but returned {0}
       .'''.format(type(result))

# Type check tweet.get_nth_tweet
result = tweet.get_nth_tweet('Test 123', 1)
assert isinstance(result, str), \
       '''tweet.get_nth_tweet should return a str, but returned {0}
       .'''.format(type(result))


# Get the final values of the constants
constant_1_after = [tweet.MAX_TWEET_LENGTH]
constant_2_after = [tweet.HASH]

# Check whether the constants are unchanged.
assert constant_1_before == constant_1_after, \
       '''Your function(s) modified the value of constant MAX_TWEET_LENGTH
       Edit your code so that the value of the constant is not 
       changed by your functions.'''
    
assert constant_2_before == constant_2_after, \
       '''Your function(s) modified the value of constant HASH
       Edit your code so that the value of the constant is not 
       changed by your functions.'''
    

our_print("""

The type checker passed.

This means that the functions in tweet.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")
