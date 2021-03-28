from flask import Flask

api = Flask(__name__)

@api.route("/files")
def upload_file(filename):
    
    res = "You successfully uploaded file"
    
    return res
