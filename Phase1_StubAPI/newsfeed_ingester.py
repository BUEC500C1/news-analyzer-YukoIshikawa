from flask import Flask

api = Flask(__name__)

@api.route("/newsfeed_ingester/keyword")
def search_keyword(keyword):

    text = "Today is a good day"
    
    return text

@api.route("/newsfeed_ingester/sentiment")
def search_sentiment(sentiment):
    
    text = "I'm happy"
    
    return text

@api.route("/newsfeed_ingester/date")
def search_date(date):
    
    text = "Today is an election day"
    
    return text
	