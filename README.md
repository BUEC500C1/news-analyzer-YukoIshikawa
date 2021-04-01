# Newsfeed Analyzer
## __Note__
- File Uploader: http://ec2-3-131-91-4.us-east-2.compute.amazonaws.com:80/ <br/>
- Newsfeed Ingester: http://ec2-3-19-67-214.us-east-2.compute.amazonaws.com:443/ <br/>
- NLP Analyzer: http://ec2-3-131-91-4.us-east-2.compute.amazonaws.com:443/ <br/>
__If you cannot access links above, please let me know so that I can connect AWS ec2 again.__ <br/>
__For more details about how to use, please check links of modules__ <br/>

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

##  Reference 
https://flask-restful.readthedocs.io/en/latest/　<br>
https://github.com/public-apis/public-apis　<br>
https://flask.palletsprojects.com/en/1.0.x/api/#module-flask.json <br>
