## =============================================
## Secure File Uploader
## =============================================
def Uploadfile():
      return "Success" 

def pdf_upload(fname):
      file_path = "temp"
      return Uploadfile(file_path, fname)

def docx_upload(fname):
      file_path = "temp"
      return Uploadfile(file_path, fname)

def csv_upload(fname):
      file_path = "temp"
      return Uploadfile(file_path, fname)
  
def txt_upload(fname):
      file_path = "temp"
      return Uploadfile(file_path, fname)
    
## =============================================
## News Feed Ingester
## =============================================

def discover_content(content):
      return "Found"

def saveArticle(article):
      return "Success"

def ingestStatus(content):
      return discover_content(content)
  
def NewYorkTimes_ingester(content):
      article = "temp"
      return saveArticle(article)
    
def WashingtonPost_ingester(content):
      article = "temp"
      return saveArticle(article)
    
def WallStreetJournal_ingester(content):
      article = "temp"
      return saveArticle(article)

## =============================================
## News Feed Ingester
## =============================================  

def FindSentiment(sentiment):
      return "Found"

def FindKeyword(keyword):
      return "Found"

def FindRelation(relation):
      return "Found"
      
def keyword_analysis(keyword):
    return FindKeyword(keyword)
  
def sentiment_analysis(sentiment):
    return FindSentiment(sentiment)
    
def relation_analysis(relation):
    return FindRelation(relation)
