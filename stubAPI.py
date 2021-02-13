## =============================================
## Secure File Uploader
## =============================================
def Uploadfile():
      return "Success" 

def pdf_upload(fname):
      return Uploadfile(file_path, fname)

def docx_upload(fname):
      return Uploadfile(file_path, fname)

def csv_upload(fname):
      return Uploadfile(file_path, fname)
  
def txt_upload(fname):
      return Uploadfile(file_path, fname)
    
## =============================================
## News Feed Ingester
## =============================================

def descover_content(content):
      return "Found"
def saveArticle(article):
      return "Success"

def ingestStatus(content):
      return discover_content(content)
  
def NewYorkTimes_ingester(content):
      return saveArticle(article)
    
def WashingtonPost_ingester(content):
      return saveArticle(article)
    
def WallStreetJournal_ingester(content):
      return saveArticle(article)

## =============================================
## News Feed Ingester
## =============================================  

def FindSentiment(sentiment):
      return "Found"
def FindeKeyword(keyword):
      return "Found"
def FindRelation(relation):
      return "Found"
      
def keyword_analysis(keyword):
    return Findkeyword(keyword)
  
def sentiment_analysis(sentiment):
    return FindSentiment(sentiment):
    
def relation_analysis(relation):
    return FindRelation(relation)
