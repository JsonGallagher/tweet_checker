# TO DO
# prompt user for tweet
# calc length of tweet
# calc if longer than the 140 max allowed characters
# evaluate if tweet is with the max allowed characters, display num of extra characters.

max_chars = 140

print("Welcome to the tweet checkr!")
tweet = input("Enter your tweet: ")
tweet_length = len(tweet)
char_over = tweet_length - max_chars

if tweet_length < max_chars:
    print(f"That {tweet_length} character tweet will work.")
else:
    print(f"Your {tweet_length} character tweet is {char_over} characters too long to tweet.")