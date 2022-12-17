#Imports
import tweepy
import schedule
import time
import pyttsx3
import subprocess


print("                                               🤖TWITTER POSTING BOT🤖")

#Set up the Twitter API by providing the necessary keys and tokens
consumer_key = 'D8sH2wuP2kMMjEKwqhxCY3uSM'
consumer_secret = 'chZAOEBvq1FDqa7Nb3zFrJRa55Jypd7ZA1sf7jwfdsCXKL4lsf'
access_token = '1551508815798865920-jyBhv7DlsQJFF92XykK2skALEoz6qv'
access_token_secret = 'SUlX2rMcezE0SvqI8HpW0Qy2ivmyNnOBQKSbE1Dta9EDV'
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
    API.update_status ('“A room without books is like a body without a soul.” - Marcus Tullius Cicero')
    API.update_status ('“Be who you are and say what you feel, because those who mind dont matter, and those who matter dont mind.” - Bernard M. Baruch')
    API.update_status ('“Youve gotta dance like theres nobody watching, Love like youll never be hurt, Sing like theres nobody listening, And live like its heaven on earth.” - Willian W. Purkey ')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    subprocess.call(["shutdown", "/s"])
    
def wednesday():
    #Tweet Inputs
    API.update_status ('“Live as if you were to die tomorrow. Learn as if you were to live forever.” - Mahatma Gandhi') 
    API.update_status ('“Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that.” - Martin Luther King Jr.')
    API.update_status ('“Without music, life would be a mistake.” - Friedrich Nietzsche')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    subprocess.call(["shutdown", "/s"])
    
def thursday():
    #Tweet Inputs
    API.update_status ('“I am so clever that sometimes I do not understand a single word of what I am saying.” - Oscar Wilde') 
    API.update_status ('“To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.” - Ralph Waldo Emerson')
    API.update_status ('“Insanity is doing the same thing, over and over again, but expecting different results.”')
    
    print("Tweet posted!")
    speak("Tweet posted!")
    exit()
        
def friday():
    #Tweet Inputs
    API.update_status ('“It is better to be hated for what you are than to be loved for what you are not.” - Andre Gide') 
    API.update_status ('“Twenty years from now you will be more disappointed by the things that you did not do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover.” - H. Jackson Brown Jr.')
    API.update_status ('“It is not a lack of love, but a lack of friendship that makes unhappy marriages.” - Friedrich Nietzsche')
    
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
   


 