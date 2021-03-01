from flask import Flask, abort, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# test data 
articles = [
{
 "ID": "",
 "title": "",
 "URl" : "",
 "author" : "", 
 "publisher" : "",
 "publication_date" : "",
 "metadata":"",
 "NLP_analysis" : "",
 }
]

@app.route('/', methods=['GET'])
def get_book(book_id):
    return jsonify(news_articles)

@app.route('/', methods=['POST'])
def makeANewNewsArticles(title, author, genre):
   articles.append(request.get_json())
   return '', 204

@app.route('/', methods=['PUT'])
def updateNewsArticles(id, title, author, genre):
    return 'Updated NewsArticles'

@app.route('/', methods=['DELETE'])
def deleteANewsArticles(id):
	delete(articles)
    return 'Removed NewsArticles'
 
