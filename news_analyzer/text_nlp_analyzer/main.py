
Request_headers : {
    "File_ID" : (file_id, type=str)
    "File_URI" : (file_uri, type=str)
    "Text" : (raw.txt, type=array)
    "Analyses" : (analyses, type=list) {
        [analysis wanted, type=bool]
    }
}

def text_nlp_analysis(Request_headers)
    Response_headers : {
        "File_ID" : (file_id, type=str) # given
        "File_URI" : (file_uri, type=str) # given
        "Analyses" : (analyses, type=object) { # generated
            "Sentiment" : (sentiment, type=str)
            "Keywords" : (keywords, type=list)
            [other analyses results]
        }
    }
    return Response_headers
