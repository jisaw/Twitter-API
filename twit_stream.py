__author__ = 'jakesawyer'

import sys
import tweepy
import logging as log
import urllib2
import json

OAUTH_TOKEN = '17796749-MPGh0m8blE7YJGcmZNG6iRgioyHOeQdzE0L8yaNIq'
OAUTH_SECRET = 'Xo9WgvMMu5DgvH62GjBCF7pgSh8qD7HRUoJICY65R7Ts4'
CONSUMER_KEY = 'Ny9DPm7eXF8R4Fk7djJdf8iUT'
CONSUMER_SECRET = 'E1DlM4wAsqbWSkJdPMQ4gkuGfkA4ioOiGVfLDXh8pIZb2te5wr'


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status


def main():
    """
    Query should look like [python twit_rest.py '"This is exact search" this is not'? 10] the ? ending the query and the following number being the limit.
    :return:
    """
    l = StdOutListener()
    to_write = []
    param = ' '.join(sys.argv[1:])
    q = param[:param.find('?')]
    #num = int(param[param.find('?')+1:])
    print param
    print q
    #print num
    log.debug('Parameter Passed: ', param)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
    try:
        stream = tweepy.Stream(auth, l)
        query = urllib2.quote(q.encode('utf8'))
        print('Query: ' + query)
        #max_tweets = num
        stream.filter(track=['%s' % query])
    except:
        log.warning('Cought Exception')
    #write_xml(to_write)

def write_xml(data):
    #TO-DO: write the data to an xml tree and save in a file
    print('Working on it')


if __name__ == "__main__":
    main()