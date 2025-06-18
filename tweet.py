import tweepy

CONSUMER_KEY = "wtmTrDWnmgQvDN0FOjCBzSI7G"
CONSUMER_SECRET = "6LH1ToFoXpkBFDJLLQMETNpGcWdtHxUXNWWMzgSlIC7P0JYpoj"

tweet_text = "Hello how are you i am kalyan"

try:
    oauth1_user_handler = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, callback="oob"
    )

    authorization_url = oauth1_user_handler.get_authorization_url()
    print(f"Please open this URL in your browser: {authorization_url}")

    verifier = input("Input PIN: ")

    access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)

    client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=access_token,access_token_secret=access_token_secret,)

    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")

except tweepy.TweepyException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")