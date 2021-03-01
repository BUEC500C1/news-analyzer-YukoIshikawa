from flask import Flask, abort, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# test data 
texts = [
{
 "file_id": "",
 "file_name": "",
 "file_URI" : "",
 "file_type" : "", 
 "metadata" : "",
 "author" : "",
 "publisher" : "",
 "publication_date" : "",
 "NLP_analysis" : "",
 }
]

@app.route('/', methods=['GET'])
def getText():
    return jsonify(texts)

@app.route('/', methods=['POST'])
def makeNewText():
   texts.append(request.get_json())
   return '', 204

@app.route('/', methods=['PUT'])
def updateText():
    return 'Updated Texts'

@app.route('/', methods=['DELETE'])
def deleteText(id):
	delete(texts)
    return 'Removed Texts'
