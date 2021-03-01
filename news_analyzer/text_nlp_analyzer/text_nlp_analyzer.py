from flask import Flask, abort, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# test data 
NLP = [
{
 "file_ID": "",
 "file_name": "",
 "file_URI" : "",
 "file_type" : "", 
 "sentiment" : "",
 }
]

@app.route('/', methods=['GET'])
def getNLP():
    return jsonify(NLP)

@app.route('/', methods=['POST'])
def makeNLP():
   NLP.append(request.get_json())
   return '', 204

@app.route('/', methods=['PUT'])
def updateNLP():
    return 'Updated NLP'

@app.route('/', methods=['DELETE'])
def deleteNLP(id):
	delete(NLP)
    return 'Removed NLP'
