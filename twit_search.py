import argparse
import tweepy
import urllib2
import dicttoxml
import json

OAUTH_TOKEN = 'xxxxxx'
OAUTH_SECRET = 'xxxxxx'
CONSUMER_KEY = 'xxxxxx'
CONSUMER_SECRET = 'xxxxxx'


class StdOutListener(tweepy.StreamListener):
    def __init__(self,limit, api=None):
        """

        :param api:
        :param limit:
        """
        super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.write_list = []
        self.limit = limit

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        decoded = json.loads(data)
        self.write_list.append(decoded)
        self.num_tweets += 1
        if self.num_tweets < int(self.limit):
            print ''
            return True
        else:
            print(self.num_tweets)
            return False

    def on_error(self, status):
        print status

def main():
    results = parse_args()
    logic(results)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', action="store", dest="query", help='Single word (-q iphone) or String (-q "car phone")')
    parser.add_argument('-l', action="store", dest="limit", help="Number of tweets returned (-l 500)", type=int)
    parser.add_argument('--file', action="store", dest="fileName", help='Name of the output file (--file file004)')
    parser.add_argument('-xml', action="store_const", dest="fileType", const="xml")
    parser.add_argument('-json', action="store_const", dest="fileType", const="json")
    parser.add_argument('--method', action="store", dest='method', help='REST of streaming API. Default is REST')
    results = parser.parse_args()
    return results


def logic(results):
    query = results.query
    limit = results.limit
    file_name = results.fileName
    file_type = results.fileType
    method = results.method
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
    if method == 'rest':
        api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())
        formatted_query = urllib2.quote(query.encode('utf8'))
        print('Query: ' + query)
        max_tweets = limit
        results = api.search(q=formatted_query, count=max_tweets)
    elif method == 'streaming':
        l = StdOutListener(limit)
        stream = tweepy.Stream(auth, l)
        stream.filter(track=['%s' % query])
        results = l.write_list
    else:
        print("Please choose 'rest' or 'streaming' for method")

    if not file_name:
        file_name = query.replace(" ", "_")
        file_name = file_name.replace("(", "")
        file_name = file_name.replace(")", "")
        file_name = file_name.replace(":", "")

    if file_type == "json":
        write_json(results, file_name)
    elif file_type =="xml":
        write_xml(results, file_name)
    else:
        print("Unknown data type. Please use either 'xml' or 'json'")

def write_xml(data, file_name):
    #TO-DO: write the data to an xml tree and save in a file
    print('Working on it')
    tree = dicttoxml.dicttoxml(data)
    f = open("data/" + file_name + ".xml", 'a')
    print >> f, tree
    f.close()

def write_json(data, file_name):
    print('workin on it')
    f = open("data/" + file_name + ".json", "a")
    print >> f, data
    f.close()



if __name__ == "__main__":
    main()
