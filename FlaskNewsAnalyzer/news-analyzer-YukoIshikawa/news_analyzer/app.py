from flask import Flask, jsonify, request

app = Flask(__name__)

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
def showtext():
  return jsonify(texts)

@app.route('/add_texts', methods=['POST'])
def editText():
  texts.append(request.get_json())
  return '', 204
  
@app.route('/update', methods=['PUT'])
def updateText():
    return 'Updated Texts'

@app.route('/', methods=['DELETE'])
def deleteText(id):
    return 'Removed Texts'

if __name__ == "__main__":
    app.run(debug=True)
    
    
