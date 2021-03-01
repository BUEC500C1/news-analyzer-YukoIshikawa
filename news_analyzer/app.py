from flask import Flask

app = Flask(__name__)
api = Api(app)

@app.route("/")
@app.route("/index")
def index():
    return 'Hello world!'


@app.route("/newsfeed_search")
def newsfeed_search():
    return 'news feed search'


@app.route("/securefile_uploader")
def secure_file_uploader_ingester():
    return 'secure_file_uploader_ingester'


@app.route("/text_nlp_analyzer")
def text_nlp_analyzer():
    return 'text_nlp_analysis'


if __name__ == "__main__":
    app.run(debug=True)
