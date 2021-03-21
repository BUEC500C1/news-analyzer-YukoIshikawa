import os
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'FlaskNewsAnalyzer.db')
)

# Everytime terminate application context, close DB
from .db import close_db
app.teardown_appcontext(close_db)

# read index page
import FlaskNewsAnalyzer.views

# add login 
import FlaskNewsAnalyzer.auth
app.register_blueprint(auth.bp)

# add upload
import FlaskNewsAnalyzer.upload
app.register_blueprint(upload.bp)

# add pdf_convert
import FlaskNewsAnalyzer.pdf_convert
app.register_blueprint(pdf_convert.bp)

# add newsfeed_ingester
import FlaskNewsAnalyzer.newsfeed_ingest
app.register_blueprint(newsfeed_ingest.bp)

import FlaskNewsAnalyzer.nlp
app.register_blueprint(nlp.bp)

