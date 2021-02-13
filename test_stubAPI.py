from stubAPI import *
import pytest 
  
## =============================================
## Secure File Uploader
## =============================================
def test_pdf_upload(fname):
      assert pdf_upload("anything") == "Success"

def test_docx_upload(fname):
      assert docx_upload("anything") == "Success"

def test_csv_upload(fname):
      assert csv_upload("anything") == "Success"
  
def test_txt_upload(fname):
      assert txt_upload("anything") == "Success"
    
## =============================================
## News Feed Ingester
## =============================================

def test_ingestStatus(content):
      assert ingestStatus("anything") == "Found"
  
def test_NewYorkTimes_ingester(content):
      assert NewYorkTimes_ingester("anything") == "Success"
    
def test_WashingtonPost_ingester(content):
      assert WashingtonPost_ingester("anything") == "Success"
     
def test_WallStreetJournal_ingester(content):
      assert WallStreetJournal_ingester("anything") == "Success"

## =============================================
## News Feed Ingester
## =============================================  
      
def test_keyword_analysis(keyword):
    assert keyword_analysis("anything") == "Found"
  
def test_sentiment_analysis(sentiment):
    assert sentiment_analysis("anything") == "Found"
    
def test_relation_analysis(relation):
    assert relation_analysis("anything") == "Found"
