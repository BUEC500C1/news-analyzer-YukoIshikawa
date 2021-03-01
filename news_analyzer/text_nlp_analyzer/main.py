Request_headers : {
    "file_ID" : (file_id, type=str)
    "file_URL" : (file_url, type=str)
    "text" : (raw.txt, type=array)
    "analysis" : (analyses, type=list) { [analysis wanted, type=bool]
    }
}

def text_nlp_analysis(Request_headers)
    Response_headers : {
        "file_ID" : (file_id, type=str) # given
        "file_URL" : (file_uri, type=str) # given
        "analysis" : (analyses, type=object) { # generated
            "sentiment" : (sentiment, type=str)
            "keywords" : (keywords, type=list) { [other analyses results]
        }
    }
    return Response_headers
