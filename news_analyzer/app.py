from flask import Flask

app = Flask(__name__)
api = Api(app)

@app.route("/")
@app.route("/index")
def index():
    return 'Hello world!'

@app.route("/newsfeed_search")
def newsfeed_ingester():
    return 'newsfeed_ingester'

@app.route("/securefile_uploader")
def secure_file_uploader_ingester():
    return 'securefile_uploader'

@app.route("/text_nlp_analyzer")
def text_nlp_analyzer():
    return 'text_nlp_analyzer'

if __name__ == "__main__":
    app.run(debug=True)
