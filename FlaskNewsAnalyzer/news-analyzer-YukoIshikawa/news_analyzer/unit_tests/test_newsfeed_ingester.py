from newsfeed_ingester import *
import pytest

def test_getArticle():
  assert getArticle() = [
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

def test_makeNewsArticle():
  assert makeNewsArticle() == ''
  
def test_updateNewsArticle():
  assert updateNewsArticle() == 'Updated NewsArticles'
  
def deleteNewsArticle():
  assert deleteNewsArticle() == 'Removed NewsArticles'
