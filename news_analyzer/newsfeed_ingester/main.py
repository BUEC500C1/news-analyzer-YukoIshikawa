Request_headers: {
    "file" : {
        "file_id
        "file_name": (file_name, type=str)
        "file_URI" : (file_uri, type=str)
        "file_type" : (file_type, type=str) 
        "metadata" : (metadata, type=object) {
            "author" : (author, type=str)
            "publisher" : (publisher, type=str)
            "publication_date" : (publication_date, type=object){
            }
        "NLP_analysis" : (analyses, type=list) { [from NLP analyzer]
        }
        }
    }
}
 
 def newsfeed_ingester(file_URI, filetype):
        Response_headers: {
            "Text": (text, type=object){
                "Text" : (raw.txt, type=array)
            }
            "Status" : (status, type=object) {
                "Ingester_status": (ingester_status, type=str)
            }
        }

   return Response_headers
