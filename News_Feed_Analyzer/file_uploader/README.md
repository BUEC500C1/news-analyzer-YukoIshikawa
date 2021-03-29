# File Uploader
## Introduction 
This is a Entity based API to upload PDFs to a local directory, extract PDF metadata and text, add file data info to DB and search for file data in DB with keywords. 

## User Story 
As an investigator, I want to upload pdf file <br/>
As an investigator, I want to convert file types (from PDF to text) <br/>
As an investigator, I want to know the uploading status (success or fail) <br/>
As an investigator, I want to add PDF metadata and converted text to DB <br/>
As an investigator, I want to search for files in DB with keywords <br/>

## Usage
- enndpoint(/upload):  upload PDF file to the directory
- endpoint(/pdf_info/< path >) : extract PDF metadata (title/author) 
- endpoint(/text/< path >) : extract text from PDF 
- endpoint(/create/< path >) : create a new DB entry
- endpoint(/add/< path >) : add new file data to database

## Sample data output 
< PDF metadata >
![image](https://user-images.githubusercontent.com/32304880/112895537-449ed780-90ab-11eb-8cad-a55d1e11b69e.png)

{   
  "author": "sarah",   
  "title": "Format for reviewing an article"  
}   
 
< text > 
![image](https://user-images.githubusercontent.com/32304880/112895640-5ed8b580-90ab-11eb-87bd-ddad0de5630d.png)

Sample format, Page 2 of 2 Additional Considerations: A literature review is a summary of what research has been completed in a topic area; it should be summarized in your own words. Read the entire article first and the n go back and take notes. Jot down notes in your own words. This increases comprehension as well as decreases the likelihood of plagiarism. Unless stated otherwise, a literature review ideally reflec t s articles published in the last five to ten years. Not every detail or fact needs to be reported. A reader will obtain a copy of the article if more information is needed. Write the literature review in the past tense; the research has already been compl eted. study. The above format is a guideline. It may be necessary to change the verbs or to expand an idea.
  
< DB entry > id will be added when the data is stored into DB
![image](https://user-images.githubusercontent.com/32304880/112888444-59c33880-90a2-11eb-8c57-23291c1a79ef.png)
![image](https://user-images.githubusercontent.com/32304880/112895945-c7279700-90ab-11eb-918f-39d06a00cb46.png)
{    
  "author": "sarah",   
  "id": "",   
  "name": "sample1",   
  "sentiment": "negative",   
  "sentiment_magnitude": 3.799999952316284,   
  "sentiment_score": -0.10000000149011612,   
  "text": "Sample format, \nPage \n2\n \nof \n2\n \nAdditional Considerations:\n \n\n \nA literature review is a summary of what research has been completed in a topic area; it should be \nsummarized in your own words.\n \n\n \nRead the entire article first and the\nn go back and take notes. Jot down notes in your own words. \nThis increases comprehension as well as decreases the likelihood of plagiarism. \n \n\n \n\n \n\n \nUnless stated otherwise, a literature review \nideally \nreflec\nt\ns\n \narticles published in the last five \nto ten \nyears.\n \n\n \nNot every detail or fact needs to be reported. A reader will obtain a copy of the article if more \ninformation is needed.\n \n\n \nWrite the literature review in the past tense; the research has already been compl\neted.\n \n\n \n\nstudy.\n \n\n \nThe above format is a guideline. It may be necessary to change the verbs or to expand an idea.\n \n \n",   
  "title": "Format for reviewing an article",   
  "upload_date": "2021-03-26"  
}      

