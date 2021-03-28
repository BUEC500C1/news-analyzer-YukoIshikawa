from flask import Flask

api = Flask(__name__)

@api.route("/nlp_analysis/sentiment" )
def analyze_sentiment(text):
    sentiment_score = -1
    return sentiment_score
	
@api.route("/nlp_analysis/entities" )	
def analyze_entities(text):
    keyword = "Location"
    return keyword