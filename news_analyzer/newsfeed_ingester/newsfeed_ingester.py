class News_articles(Base):
  __tablename__ = 'news_articles'

  id = Column(Integer, primary_key=True)
  title = Column(String(250), nullable=False)
  author = Column(String(250), nullable=False)
  genre = Column(String(250))

  @property
  def serialize(self):
     return {
        'title': self.title,
        'author': self.author,
        'genre': self.genre,
        'id': self.id,
     }
    
  def get_news_articles():
   news_articles = session.query(News_articles).all()
   return jsonify(news_articles= [n.serialize for n in news_articles])

def get_news_articles(news_articles_id):
   news_articles = session.query(News_articles).filter_by(id = news_articles_id).one()
   return jsonify(news_articles = news_articles.serialize)

def makeANewBook(title,author, genre):
   addednews_articles = News_articles(title=title, author=author,genre=genre)
   session.add(addednews_articles)
   session.commit()
   return jsonify(News_articles=addednews_articles.serialize)

def updateBook(id,title,author, genre):
   updatednews_articles = session.query(News_articles).filter_by(id = id).one()
   if not title:
       updatednews_articles.title = title
   if not author:
       updatednews_articles.author = author
   if not genre:
       updatednews_articles.genre = genre
   session.add(updatednews_articles)
   session.commit()
   return 'Updated a news_articles with id %s' % id

def deleteABook(id):
   news_articlesToDelete = session.query(News_articles).filter_by(id = id).one()
   session.delete(news_articlesToDelete)
   session.commit()
   return 'Removed news_articles with id %s' % id
 
