from flask import Flask, flash, request, redirect, render_template, json, jsonify, url_for
from google.cloud import language_v1
from app import app
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'high-mountain-308101-7fe5259b2655.json'

@app.route("/")
def index():
    return "NLP Analyzer"

@app.route("/nlp/<text_content>", methods=["GET"])
def analyze_nlp(text_content):

    client = language_v1.LanguageServiceClient()
    
    type_ = language_v1.Document.Type.PLAIN_TEXT
    
    language = "en"
    
    document = {"content": text_content, "type_": type_, "language": language}
    
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})

    nlp = {
        "sentiment_score": "",
        "sentiment_magnitude": "",
        "sentiment": ""
        }

    nlp["sentiment_score"] = response.document_sentiment.score
    nlp["sentiment_magnitude"] = response.document_sentiment.magnitude
    
    if response.document_sentiment.score < 0:
        nlp["sentiment"] = "negative"
    elif response.document_sentiment.score > 0:
        nlp["sentiment"] = "positive"
    else:
        nlp["neutral"] = "neutral"

    return jsonify(nlp)

if __name__ == "__main__":
   ## app.run(debug=True)
   app.run(host='0.0.0.0', port=443)