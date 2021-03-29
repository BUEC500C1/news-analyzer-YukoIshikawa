# NLP Analyzer
## Introduction 
This is a Entity based API to analyze nlp.

## User Story 
As an investigator, I want to find semtiment score of text content <br/>
As an investigator, I want to find sentiment magnitude of text content <br/>
As an investigator, I want to find sentiment (positive, negative or neutral) <br/>
As an investigator, I want to add nlp analysis to file data in DB <br/>

## Note
To use this module, you need authenticate to a Google Cloud API and set an environment variable where your code runs
[link](https://cloud.google.com/docs/authentication/getting-started)

## Detail
- endpoint(/nlp/< text content >): analyze nlp (sentiment score, sentiment magnitude and sentiment)

## sample NLP output 
(sample text content: I want to be an engineer) <br> 
![image](https://user-images.githubusercontent.com/32304880/112894936-811e0380-90aa-11eb-9545-bf36f2159ef6.png)

{  
  "sentiment": "positive",   
  "sentiment_magnitude": 0.8999999761581421,   
  "sentiment_score": 0.8999999761581421  
}  

