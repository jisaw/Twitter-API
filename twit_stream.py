__author__ = 'jakesawyer'

import sys
import tweepy
import logging as log
import urllib2
import json
import xml.etree.cElementTree as ET

OAUTH_TOKEN = '17796749-MPGh0m8blE7YJGcmZNG6iRgioyHOeQdzE0L8yaNIq'
OAUTH_SECRET = 'Xo9WgvMMu5DgvH62GjBCF7pgSh8qD7HRUoJICY65R7Ts4'
CONSUMER_KEY = 'Ny9DPm7eXF8R4Fk7djJdf8iUT'
CONSUMER_SECRET = 'E1DlM4wAsqbWSkJdPMQ4gkuGfkA4ioOiGVfLDXh8pIZb2te5wr'

param = ' '.join(sys.argv[1:])
q = param[:param.find('?')]
num = int(param[param.find('?')+1:])


class StdOutListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.write_list = []

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        self.write_list.append([decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')])
        self.num_tweets += 1
        if self.num_tweets < int(num):
            print ''
            return True
        else:
            print(self.num_tweets)
            return False

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
    num = int(param[param.find('?')+1:])
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
    filename = q.replace(" ", "_")
    filename = filename.replace("(", "")
    filename = filename.replace(")", "")
    filename = filename.replace(":", "")
    write_xml(l.write_list, filename)

def write_xml(data, file_name):
    #TO-DO: write the data to an xml tree and save in a file
    print('Working on it')
    thread = ET.Element('thread')
    for tweet in data:
        author = ET.SubElement(thread, 'author')
        author.text = str(tweet[0])

        text = ET.SubElement(thread, 'text')
        text.text = str(tweet[1])

    f = open("data/" + file_name + "streaming" + ".xml", 'a')
    with f:
        tree = ET.ElementTree(thread)
        tree.write(f)
    f.close()

if __name__ == "__main__":
    main()