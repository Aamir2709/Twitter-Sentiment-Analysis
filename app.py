from flask import Flask,request,render_template
import main
app = Flask(__name__,template_folder='template')
from flask_cors import CORS,cross_origin

@app.route('/',methods=['POST','GET'])
def index():
    try:
        if request.method == "POST":
            tweet_topic = request.form.get("tweet_topic")
            search_tweets = main.get_tweets(tweet_topic)
            sports_tweets = main.get_tweets('sports')
            news_tweets = main.get_tweets('news')
            entertainment_tweets = main.get_tweets('entertainment')
            trending_tweets = main.get_tweets('trending')
            return render_template("index.html",sports_tweets=sports_tweets,news_tweets=news_tweets,entertainment_tweets=entertainment_tweets,trending_tweets=trending_tweets,search_tweets=search_tweets,tweet_topic=tweet_topic)
        sports_tweets = main.get_tweets('sports')
        news_tweets = main.get_tweets('news')
        entertainment_tweets = main.get_tweets('entertainment')
        trending_tweets = main.get_tweets('trending')
        return render_template("index.html",sports_tweets=sports_tweets,news_tweets=news_tweets,entertainment_tweets=entertainment_tweets,trending_tweets=trending_tweets)
    except:
        return render_template("error.html")

if __name__=="__main__":
    app.run()
