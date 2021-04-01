# Newsfeed Ingester
## Introduction 
This is a Entity based API to ingest newsfeed with keywords, add it into DB and search for articles with keywords. 

## User Story 
As an investigator, I want to discover content from Web to enhance story <br/>
As an investigator, I want to conduct keyword searches and ingest relevant articles <br/>
As an investigator, I want to add articles into DB for future works <br/>
As an investigator, I want to search for articles in DB with entered keyword <br/>

## Note
To use this module, you need to get API key and put your API key *APIKEY = 'ENTER YOUR API KYE HERE'*

## Usage
- < :443/ >: index page
- < :443/article/<keyword> >: show the most relevant article with the keyword you provided  
- < :443/article/create/< keyword > >: create a new DB entry and add it to DB
- < :443/article/search/< keyword > >: search for the article relevant to the keyword and show it
- < :443/article/delete/< article_id > >: delete the article of article_id

## Public API 
[News API](https://newsapi.org/) is used for this module to search worldwide news articles and access JSON API.

## Sample output data (keyword: Covid) 
![image](https://user-images.githubusercontent.com/32304880/112888561-7eb7ab80-90a2-11eb-9b7e-6740776c16b7.png)
![image](https://user-images.githubusercontent.com/32304880/112896083-f76f3580-90ab-11eb-880d-9c17ce0fbd9d.png)
