import datetime
from twitter import TwitterStream, OAuth

__author__ = 'jakesawyer'

OAUTH_TOKEN = '17796749-MPGh0m8blE7YJGcmZNG6iRgioyHOeQdzE0L8yaNIq'
OAUTH_SECRET = 'Xo9WgvMMu5DgvH62GjBCF7pgSh8qD7HRUoJICY65R7Ts4'
CONSUMER_KEY = 'Ny9DPm7eXF8R4Fk7djJdf8iUT'
CONSUMER_SECRET = 'E1DlM4wAsqbWSkJdPMQ4gkuGfkA4ioOiGVfLDXh8pIZb2te5wr'


ts = TwitterStream(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
openstream = ts.statuses.filter(track='iPhone 6')
with open("twit_data.txt", "w") as f:
  for item in openstream:
    response = ('User: %s\nText: %s\nFavorited: %s\nRetweets: %s\nTime: %s' %(item['user']['screen_name'], item['text'], item['favorited'], item['retweeted'], item['created_at'])).encode('utf-8')
    f.write(response)
    print(response + '\n')
  f.close()
  #for i in item:
    #print(i)
  #print(" \n")
  #print item['user']['screen_name'], item['created_at'], '%a %b %d %H: %M: %S  + 0000 %Y', item[
  # 'text']

#WHAT YOU CAN GET FROM EACH TWEET
#favorited
#contributors
#truncated
#text
#possibly_sensitive
#in_reply_to_status_id
#user
#filter_level
#geo
#id
#favorite_count
#lang
#retweeted_status
#entities
#in_reply_to_user_id_str
#retweeted
#coordinates
#timestamp_ms
#source
#in_reply_to_status_id_str
#in_reply_to_screen_name
#id_str
#extended_entities
#place
#retweet_count
#created_at
#in_reply_to_user_id