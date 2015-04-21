'''
Created on Apr 16, 2015

@author: rajiv
'''
from bottle import Bottle, run, route, response, hook
import tweetRepository as tr

myApp = Bottle()

@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@route('/getTopTweets/<sym>')
def getTopTweetsbySymbol(sym):
    topTweets = tr.get_top_tweets(sym)
    response.content_type = 'application/json'
    return topTweets

@route('/getAllTweets/<sym>')
def getAllTweetsbySymbol(sym):
    tweets = tr.get_all_tweets(sym)
    return tweets

@route('/getSentimentCount/<sym>')
def getSentimentCountbySymbol(sym):
    count = tr.get_sentiment_count(sym)
    return count

run(host = "0.0.0.0", port = 8800, interval = 1, reloader = True, debug = True)

