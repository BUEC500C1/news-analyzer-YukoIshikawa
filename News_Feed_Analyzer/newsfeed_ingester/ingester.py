from flask import Flask,render_template,request, jsonify, flash
from newsapi import NewsApiClient
from file_uploader.db import get_db
 
app = Flask(__name__)
 
APIKEY = 'ENTER YOUR API KYE HERE'   
newsapi = NewsApiClient(api_key=APIKEY)

@app.route('/')
def index():
    return render_template('newsfeed_ingester_index.html',news='')
 
@app.route('/articles/<keyword>',methods=['GET']) 
def get_article(keyword):
    news = newsapi.get_top_headlines(q=keyword,language='en', country='us')
    return news['articles'][0] # pick the most relevant article

@app.route('/articles/add/<keyword>',methods=["POST", "GET"])     
def add_article(keyword):
    news = get_article(keyword)
    db = get_db() 
    
    author = news["author"]
    title = news["title"]
    description = news["description"] 
    url = news["url"]
    urlToImage = news["urlToImage"] 
    publishedAt = news["publishedAt"]
    content = news["content"] 
    
    db.execute(
        'INSERT INTO Articles (author, title, description, url, urlToImage, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (author, title, description, url, urlToImage, publishedAt, content,)
    )
    db.commit()
    
    flash('Successfully added to DB', category='alert alert-info')
    return redirect(url_for('index'))

@app.route('/articles/search/<keyword>',methods=['POST'])       
def search_article(keyword):
    db = get_db()
    
    articles = db.execute(
        'SELECT * FROM Articles WHERE article_id = ? or author = ? or title = ? or publishedAt = ?', 
        (keyword,keyword, keyword, keyword,)
    ).fetchall()
    
    if files is None:
        return redirect('error_handler')
    else:
        return jsonify(articles) 
    
if __name__ == "__main__":
    app.run(debug=True)
