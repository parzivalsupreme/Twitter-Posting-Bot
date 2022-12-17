# Twitter-Posting-Bot

This is a Python script that uses the tweepy, schedule, and pyttsx3 libraries to automate the process of posting tweets and providing audio feedback. The script is set up to post tweets at 12:30 PM on specific days of the week and then shutdown the computer.

### Requirements

- Python 3
- tweepy
- schedule
- pyttsx3

### Setup

Install the required libraries by running pip install tweepy schedule pyttsx3.
Set up a Twitter developer account and create a new app to obtain your API keys and tokens.
Replace the placeholder values for consumer_key, consumer_secret, access_token, and access_token_secret with your own API keys and tokens.
Input your desired tweets in the designated areas in the monday(), tuesday(), wednesday(), thursday(), and friday() functions.
Run the script using python filename.py.

### Notes

The script uses the subprocess.call() function to shutdown the computer after posting the tweets. If you do not want this behavior, you can remove this line or replace it with a different command.
The script uses the pyttsx3 library to provide audio feedback when a tweet is posted. The voice used can be changed by modifying the VoiceGender variable.
The script uses the schedule library to schedule the tweet posting functions to run at a specific time on specific days of the week. You can modify the schedule by changing the time and day of the week in the schedule.every().day_of_week.at("time").do(function) lines.
