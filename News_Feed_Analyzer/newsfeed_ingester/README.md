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

## Detail
- endpoint(/articles/<<keyword>>): ingest the most relevant articles the with provided keyword  
- endpoint(/articles/add/<<keyword>>): discover an article with keywords and add it to DB 
- endpoint(/articles/search/<<keyword>>): search for articles in DB with keywords

## Public API 
[News API](https://newsapi.org/) is used for this module to search worldwide news articles and access JSON API.

## Sample output data (keyword: Covid) 
![image](https://user-images.githubusercontent.com/32304880/112888561-7eb7ab80-90a2-11eb-9b7e-6740776c16b7.png)
