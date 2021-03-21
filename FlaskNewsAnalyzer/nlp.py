
from google.cloud import language_v1
from flask import (Blueprint, flash, redirect, render_template, request, url_for, session)
from FlaskNewsAnalyzer.db import get_db

bp = Blueprint('nlp', __name__, url_prefix='/nlp')

@bp.route('/sentiment', methods=('GET', 'POST'))
def  analyze_sentiment():

    text_content = request.form['text_content']
    text_id = request.form['text_id']

    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    
    db = get_db() ## to store sentiment to DB
    for sentence in response.sentences:
        db.execute(
            'INSERT INTO sentiment (text_id, score, magnitude,) VALUES (?, ?, ?)',
            (text_id, response.document_sentiment.score, response.document_sentiment.magnitude)
        )
        db.commit()

@bp.route('/entities', methods=('GET', 'POST'))
def analyze_entities():

    text_content = request.form['text_content']
    text_id = request.form['text_id']

    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    
    db = get_db() ## to store entities to DB
    for sentence in response.sentences:
        db.execute(
            'INSERT INTO entities (text_id, entity_type, salience_score, mention_text, mention_type) VALUES (?, ?, ?, ?, ?)',
            (text_id, response.document_sentiment.score, response.document_sentiment.magnitude)
        )
        db.commit()

