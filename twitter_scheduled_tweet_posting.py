#Modules
import tweepy
import schedule
import time
import pyttsx3
import subprocess


print("                                               🤖TWITTER POSTING BOT🤖")


#Twitter API
consumer_key = 'D8sH2wuP2kMMjEKwqhxCY3uSM'
consumer_secret = 'chZAOEBvq1FDqa7Nb3zFrJRa55Jypd7ZA1sf7jwfdsCXKL4lsf'
access_token = '1551508815798865920-jyBhv7DlsQJFF92XykK2skALEoz6qv'
access_token_secret = 'SUlX2rMcezE0SvqI8HpW0Qy2ivmyNnOBQKSbE1Dta9EDV'
authenticator = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticator.set_access_token(access_token, access_token_secret)
API = tweepy.API(authenticator, wait_on_rate_limit=True)

#Text to speech 
engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
VoiceGender = engine.setProperty('voice', voices[1].id)
def speak(texttospeech):
    engine.say(texttospeech)
    engine.runAndWait()


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
    subprocess.call(["shutdown", "/s"])
    
def friday():
    #Tweet Inputs
    API.update_status ('') 
    API.update_status ('')
    API.update_status ('')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    subprocess.call(["shutdown", "/s"])
    
#Function call
schedule.every().monday.at("12:30").do(monday)
schedule.every().tuesday.at("12:30").do(tuesday)
schedule.every().wednesday.at("12:30").do(wednesday)
schedule.every().thursday.at("12:30").do(thursday)
schedule.every().friday.at("12:30").do(friday)


while True:
  schedule.run_pending()
  time.sleep(1)
   


 
