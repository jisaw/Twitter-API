import datetime
import sys
from twitter import TwitterStream, OAuth
import xml.etree.cElementTree as ET
from xml.dom import minidom

__author__ = 'jakesawyer'

OAUTH_TOKEN = '17796749-MPGh0m8blE7YJGcmZNG6iRgioyHOeQdzE0L8yaNIq'
OAUTH_SECRET = 'Xo9WgvMMu5DgvH62GjBCF7pgSh8qD7HRUoJICY65R7Ts4'
CONSUMER_KEY = 'Ny9DPm7eXF8R4Fk7djJdf8iUT'
CONSUMER_SECRET = 'E1DlM4wAsqbWSkJdPMQ4gkuGfkA4ioOiGVfLDXh8pIZb2te5wr'


def main():
    ts = TwitterStream(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    get_twit_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], ts)


def get_twit_data(search_term, num_results=0, format='xml', file_name = 'TwitAPIOut', ts=None):
    openstream = ts.statuses.filter(track='%s' % search_term)
    root = ET.Element('root')
    num = 0
    while num < num_results:
        for item in openstream:
            response = ('User: %s\nText: %s\nFavorited: %s\nRetweets: %s\nTime: %s' % (
                item['user']['screen_name'], item['text'], item['favorited'], item['retweeted'],
                item['created_at'])).encode('utf-8')
            # f.write(response)
            print(response + '\n')
            make_xml(item['user']['screen_name'], item['text'], item['favorited'], item['retweeted'],
                      item['created_at'], file_name, root)
            num += 1
    write_xml(file_name, root)


def make_xml(screen_name, text, favorited, retweets, created, file_name, root):

    s_name = ET.SubElement(root, 'screen_name')
    s_name.text = screen_name

    txt = ET.SubElement(root, 'text')
    txt.text = text

    fav = ET.SubElement(root, 'favorited')
    fav.text = favorited

    retwts = ET.SubElement(root, 'retweets')
    retwts.text = retweets

    crtd = ET.SubElement(root, 'created')
    crtd.text = created

def write_xml(file_name, root):
    f = open(file_name + '.xml', 'a')

    with f:
        tree = ET.ElementTree(root)
        tree.write(f)
    f.close()

        # for i in item:
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