# Newsfeed Analyzer
## __Note__
- File Uploader: http://ec2-3-131-91-4.us-east-2.compute.amazonaws.com:80/ <br/>
- Newsfeed Ingester: http://ec2-3-19-67-214.us-east-2.compute.amazonaws.com:443/ <br/>
- NLP Analyzer: http://ec2-3-131-91-4.us-east-2.compute.amazonaws.com:443/ <br/>
  
__If you cannot access links above, please let me know so that I can connect AWS ec2 again < yukoi@bu.edu >__ <br/>
__For more details about the usage of each module, please check below__ <br/>

## Introduction 
This repository includes an API to help journalists to create articles by uploading files, analyzing nlp and ingesting newsfeeds. <br/>
The API uses flask, AWS EC2, SQLite, Google Cloud Computing Natural Language API, and News API. 

## Project Task Milestone
Phase1[DONE]: API definition and Stub API implementation: [Phase1](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/Phase1_StubAPI)<br>
Phase2[DONE]: REST API implementation and deploy it on AWS EC2: [Phase2](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/Phase2_RestAPI) and [ec2](http://ec2-3-17-151-213.us-east-2.compute.amazonaws.com:443/)<br>
Phase3[DONE]: File uploader implementation: [link](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/News_Feed_Analyzer/file_uploader)<br>
Phase4[DONE]: Newsfeed ingester implementation: [link](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/News_Feed_Analyzer/newsfeed_ingester) <br>
Phase5[DONE]: NLP implementation: [link](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/News_Feed_Analyzer/nlp_analyzer) <br>
Code review[DONE]: [link](https://github.com/BUEC500C1/news-analyzer-dongfang98/issues/4) [link](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/issues)<br>

## Modules
- [File Uploader](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/News_Feed_Analyzer/file_uploader)
- [Newsfeed Ingester](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/News_Feed_Analyzer/newsfeed_ingester)
- [NLP Analyzer](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/News_Feed_Analyzer/nlp_analyzer) <br>
More details are in each module's page and screenshots are here [link](https://github.com/BUEC500C1/news-analyzer-YukoIshikawa/tree/master/screenshots)

## Usage
- __File Uploader__  
< :80/ >: upload PDF file to the directory  
< :80/file/metadata >: extract PDF metadata (title/author)  
< :80/file/text/ >: extract text from PDF  
< :80/file/create/< file > > : create a new DB entry and add it to DB  
      - *This includes NLP*  
      - *Please enter the file name you uploaded before or sample1.pdf*  
< :80/file/view >: show DB contents  
< :80/file/delete/< file_id > > : delete the file of file_id  
  
- __Newsfeed Ingester__  
< :443/ >: index page  
< :443/article/ >: show the most relevant article with the keyword you provided  
< :443/article/create/< keyword > >: create a new DB entry and add it to DB  
< :443/article/search/< keyword > >: search for the article relevant to the keyword and show it  
< :443/article/delete/< article_id > >: delete the article of article_id  
  
- __NLP Analyzer__  
< :443/nlp/< text content >): analyze nlp (sentiment score, sentiment magnitude and sentiment)

##  Reference 
https://flask-restful.readthedocs.io/en/latest/　<br>
https://github.com/public-apis/public-apis　<br>
https://flask.palletsprojects.com/en/1.0.x/api/#module-flask.json <br>
