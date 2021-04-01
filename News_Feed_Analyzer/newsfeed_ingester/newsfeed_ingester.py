from flask import Flask,render_template,request, jsonify, flash, redirect, abort
import logging 
from newsapi import NewsApiClient
from datetime import date
from db import get_db
 
app = Flask(__name__)
 
APIKEY = 'f9e31e950cd9484ab3fd7b069a3b39f5'   
newsapi = NewsApiClient(api_key=APIKEY)

@app.route('/')
def index():
    return "Newsfeed Ingester"
 
@app.route('/article/<keyword>',methods=['GET']) 
def get_article(keyword):
    news = newsapi.get_everything(q=keyword,language='en', sort_by='relevancy')
    if news['totalResults'] == 0:
        app.logger.info('There is no such article')
        return jsonify({"error": "There is no such article",}), 403
    else: 
        return news['articles'][0] # pick the most relevant article

@app.route('/article/create/<keyword>',methods=["POST", "GET"])     
def create_article(keyword):
    news = get_article(keyword)
    db = get_db() 
    
    author = news["author"]
    title = news["title"]
    upload_date = str(date.today())
    description = news["description"] 
    url = news["url"]
    urlToImage = news["urlToImage"] 
    publishedAt = news["publishedAt"]
    content = news["content"] 
    
    db.execute(
        'INSERT INTO Articles (keyword, author, title, upload_date, description, url, urlToImage, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (keyword, author, title, upload_date, description, url, urlToImage, publishedAt, content,)
    )
    db.commit()
    
    app.logger.info('Successfully added to DB')
    return 'Successfully added to DB', 200

@app.route('/article/search/<keyword>', methods=['GET'])       
def search_article(keyword):
    
    db = get_db()
    
    article = db.execute(
        'SELECT * FROM Articles WHERE article_id = ? or keyword = ? or author = ? or title = ? or upload_date = ? or publishedAt = ?', 
        (keyword, keyword, keyword, keyword, keyword, keyword,)
    ).fetchone()
    
    if article is None:
        app.logger.info('There is no such article')
        return jsonify({"error": "There is no such article",}), 403
    else:
        return jsonify(article)
        
@app.route('/article/delete/<article_id>', methods=['GET', 'POST'])       
def delete_article(article_id):
    db = get_db()
    article = db.execute(
        'SELECT * FROM Articles WHERE article_id = ?', (article_id,)
    ).fetchone()
    if article is None:
        app.logger.info('There is no such article')
        return jsonify({"error": "There is no such article",}), 403
    else:
        db.execute('DELETE FROM Articles WHERE article_id = ?', (article_id,))
        db.commit()
        app.logger.info('Successfully deleted the article')
        return 'Successfully deleted the article', 200

@app.route('/article/view', methods=['GET'])       
def view_article():
    db = get_db()
    articles = db.execute('SELECT * FROM Articles').fetchall()
    return jsonify(articles)
    
    
if __name__ == "__main__":
    app.secret_key = "super secret key"
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=443)
