class test_SecureFileUploader():
  def test_uploadStatus(fname, ftype):
  allowed_ftype = ['pdf', 'csv', 'docx', 'txt']
  if fname == "": 
    return "Failure: No file selected"
  elif ftype not in allowed_ftype:
    return "Failure: Not allowed file type"
  else:
    print("Processing the upload")
    return [fname, ftype]

  def pdf_upload(fname):
      file_path = "{/upload/pdf/{filename}}.frame(filename = fname) 
      return Uploadfile(file_path, fname)

  def docx_upload(fname):
      file_path = "{/upload/docx/{filename}}.frame(filename = fname) 
      return Uploadfile(file_path, fname)

  def csv_upload(fname):
      file_path = "{/upload/csv/{filename}}.frame(filename = fname) 
      return Uploadfile(file_path, fname)
  
  def txt_upload(fname):
      file_path = "{/upload/txt/{filename}}.frame(filename = fname) 
      return Uploadfile(file_path, fname)
    
class NewsFeedIngester():
  def ingestStatus(content):
      return discover_content(content)
  
  def NewYorkTimes_ingester(content):
      return saveArticle(article)
    
  def WashingtonPost_ingester(content):
      return saveArticle(article)
    
  def WallStreetJournal_ingester(content):
      return saveArticle(article)
    
class TextNLPAnalysis():
  def keyword_analysis(keyword):
    return Findkeyword(keyword)
  
  def sentiment_analysis(sentiment):
    return FindSentiment(sentiment):
    
  def relation_analysis(relation):
    return FindRelation(relation);
