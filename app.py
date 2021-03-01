from flask import Flask, abort, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/newsfeed_ingester')
def newsfeed_ingester():
    return 'news feed ingester'

@app.route('/securefile_uploader')
def securefile_uploader_ingester():
    return 'secure_file_uploader_ingester'

@app.route('/text_nlp_analysis')
def text_nlp_analysis():
    return 'text_nlp_analysis'

if __name__ == "__main__":
    app.run(debug=True)
