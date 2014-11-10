import sys
import tweepy
import logging as log

OAUTH_TOKEN = '17796749-MPGh0m8blE7YJGcmZNG6iRgioyHOeQdzE0L8yaNIq'
OAUTH_SECRET = 'Xo9WgvMMu5DgvH62GjBCF7pgSh8qD7HRUoJICY65R7Ts4'
CONSUMER_KEY = 'Ny9DPm7eXF8R4Fk7djJdf8iUT'
CONSUMER_SECRET = 'E1DlM4wAsqbWSkJdPMQ4gkuGfkA4ioOiGVfLDXh8pIZb2te5wr'



def main():
    """
    Query should look like [python twit_rest.py '"This is exact search" this is not'? 10] the ? ending the query and the following number being the limit.
    :return:
    """
    param = ' '.join(sys.argv[1:])
    q = param[:param.find('?')]
    num = int(param[param.find('?')+1:])
    print param
    print q
    print num
    log.debug('Parameter Passed: ', param)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
    try:
        api = tweepy.API(auth)
        query = q
        max_tweets = num
        for tweet in tweepy.Cursor(api.search, q=query).items(max_tweets):
            print "Author: %s\nDate: %s\nText: %s\n\n" % (tweet.author.screen_name, tweet.created_at, tweet.text)
            #print tweet.created_at, tweet.text
    except:
        log.warning('Cought Exception')


if __name__ == "__main__":
    main()