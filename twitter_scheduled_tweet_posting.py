#Imports
import tweepy
import schedule
import time
import pyttsx3
import subprocess


print("                                               🤖TWITTER POSTING BOT🤖")

#Set up the Twitter API by providing the necessary keys and tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
authenticator = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticator.set_access_token(access_token, access_token_secret)
API = tweepy.API(authenticator, wait_on_rate_limit=True)

#Initialize the text-to-speech engine and set the voice to be used
engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
VoiceGender = engine.setProperty('voice', voices[1].id)
#Function to speak the given text using the text-to-speech engine
def speak(texttospeech):
    engine.say(texttospeech)
    engine.runAndWait()

#Functions for each day of the week that will post the tweets and provide audio feedback
def monday():
    #Tweet Inputs
    API.update_status ('') 
    API.update_status ('')
    API.update_status ('')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    subprocess.call(["shutdown", "/s"])
    
def tuesday():
    #Tweet Inputs
    API.update_status ('')
    API.update_status ('')
    API.update_status ('')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    subprocess.call(["shutdown", "/s"])
    
def wednesday():
    #Tweet Inputs
    API.update_status ('') 
    API.update_status ('')
    API.update_status ('')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    subprocess.call(["shutdown", "/s"])
    
def thursday():
    #Tweet Inputs
    API.update_status ('') 
    API.update_status ('')
    API.update_status ('')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    exit()
        
def friday():
    #Tweet Inputs
    API.update_status ('') 
    API.update_status ('')
    API.update_status ('')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    exit()
    
#Use the schedule library to schedule the functions to run at a specific time on a specific day of the week
schedule.every().monday.at("12:30").do(monday)
schedule.every().tuesday.at("12:30").do(tuesday)
schedule.every().wednesday.at("12:30").do(wednesday)
schedule.every().thursday.at("12:30").do(thursday)
schedule.every().friday.at("12:30").do(friday)

#These lines form a loop that will continually check for and run any scheduled tasks and then pause for 1 second before checking again. This allows the program to continuously run and check for scheduled tasks in the background without using up too much processing power.
while True:
  schedule.run_pending()
  time.sleep(1)
   


 
