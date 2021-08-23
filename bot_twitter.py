import tweepy
import time
import random

#here starts the autentication section, you have to replace the strings

consumer_key = "Found on the Twitter Development Portal and its personal"
consumer_secret = "Found on the Twitter Development Portal and its personal" 
access_token = "Found on the Twitter Development Portal and its personal" 
access_token_secret = "Found on the Twitter Development Portal and its personal"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)        #This function auteticates the app
auth.set_access_token(access_token, access_token_secret)        #This function stablish what the app can or can't do
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen_id.txt'
EXAMPLE = 'example.txt' #here you asign the files to variables

#This function open the file on read-only mode and pick a random line from it
def random_sentence(example):
    fr = open(example, 'r')
    lines = fr.readlines() 
    random_line = random.choice(lines) if lines else None
    fr.close()
    return str(random_line)

#This function get the last seen id on the timeline

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

#And this function stores the ID in last_seen_id.txt

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

#The main function, it keeps the bot working
def reply_to_tweets():
    print('Searching for hashtags and mentions...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended') #gets the last 20 tweets in bot's timeline
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)                                     
        #Here starts detecting the hastags in the tweets with a mention
        if '#example' in mention.full_text.lower():
            print('Hashtag found', flush=True)
            print('Replying...', flush=True)
            api.update_status('@' + mention.user.screen_name + random_sentence(EXAMPLE), mention.id)
while True:
    reply_to_tweets()
    time.sleep(15) #15 secons cooldown to not overpass the API request limit