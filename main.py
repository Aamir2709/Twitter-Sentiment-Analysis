from textblob import TextBlob
import tweepy
import requests
import json

api_key = '8NHL2FoSVp3O3YnBSBPUmEU1J'
api_key_secret  = 'XOXqsQq0xYZXKVbJrt6tg21eZ6h64bdJ1o0RSpXXrDZ9i7ykLL'
access_token = '1445367967647027207-JJnvg3Rgwr7Mfav7dyAWdF7ec2naqH'
access_token_secret = 'OiZxNYRGD8JYCpQWE8oOXFCphFkNEmdR2fepuYSPcA9OG'
'''
auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret= api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'stocks'
tweet_amount = 20

tweets = tweepy.Cursor(api.search_tweets,q=search_term,lang='en').items(tweet_amount)

for tweet in tweets:
    print(tweet.text)'''


search_url = "https://api.twitter.com/2/tweets/search/recent"

bearer_token ='AAAAAAAAAAAAAAAAAAAAAB1%2BlQEAAAAA9lan63awqKQKiF6hEwT95G1eGv0%3D9ugDOlaUE0hSO8EXRRqCof8066bKCqTMOw4LJ0ooqubZXf6rut'




def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()





#print(get_tweets_search('cricket'))

def get_tweets(topic):
    search_topic = str(topic) 
    query_params = {'query': '{} lang:en'.format(search_topic),
                'max_results':50}
    json_response = connect_to_endpoint(search_url, query_params)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    tweets = []
    polarity = 0
    positive,negative,neutral = 0,0,0
    for i in range(50):
        tweets.append(json_response['data'][i]['text'])
    #print(len(json_response['data']))
    #print(tweets[:2])
    final_tweets = {}
    final_text=''
    negative_tweets = []
    positive_tweets = []
    neutral_tweets = []
    for tweet in tweets:
        final_text = tweet.replace('RT','')
        if final_text.startswith(' @'):
            pos = final_text.index(':')
            final_text = final_text[pos+2:]
        if final_text.startswith('@'):
            pos = final_text.index(' ')
            final_text = final_text[pos+2:]
        #final_tweets.append(final_text)
    #print(final_tweets[:3])
        
        analysis = TextBlob(final_text)
        tweet_polarity = analysis.polarity
        if tweet_polarity>0.00:
            positive+=1
            final_tweets[final_text] = "Positive"
            
        elif tweet_polarity<0.00:
            negative+=1
            final_tweets[final_text] = "Negative"
        elif tweet_polarity==0.00:
            neutral+=1
            final_tweets[final_text] = "Neutral"
        polarity+=tweet_polarity
    #print(len(tweets))
    #print(len(final_tweets))
    '''print(polarity)
    print(f'Amount of positive tweets: {positive}')
    print(f'Amount of negative tweets: {negative}')
    print(f'Amount of neutral tweets: {neutral}')'''
    return final_tweets