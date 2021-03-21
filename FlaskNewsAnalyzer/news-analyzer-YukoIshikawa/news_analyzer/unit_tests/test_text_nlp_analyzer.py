from nlp_analyzer import *
import pytest

def test_getNLP():
  assert getNLP() = [
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

def test_makeNLP():
  assert makeNLP() == ''
  
def test_updateNLP():
  assert updateNLP() == 'Updated NLP'
  
def deleteNLP():
  assert deleteNLP() == 'Removed NLP'
