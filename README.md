# Twitter-Posting-Bot

This is a Python script that uses the tweepy module to post tweets to a Twitter account at a specified time each day of the week.

The script authenticates the Twitter account using the consumer_key, consumer_secret, access_token, and access_token_secret provided. It then uses the pyttsx3 module to convert text to speech and the subprocess module to shutdown the computer after the tweets are posted.

The script uses the schedule module to schedule the tweets to be posted at 12:30 PM every day of the week. The tweets to be posted are specified in the monday(), tuesday(), wednesday(), thursday(), and friday() functions. The script then enters an infinite loop, using the time.sleep() function to check for scheduled tasks at a rate of 1 second.

It is worth noting that the consumer_key, consumer_secret, access_token, and access_token_secret should be kept secret and not shared with anyone. They are used to authenticate the Twitter account and allow the script to access and modify the account.
