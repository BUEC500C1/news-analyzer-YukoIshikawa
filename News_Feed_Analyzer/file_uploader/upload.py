from flask import Flask, flash, request, redirect, render_template, json, jsonify, url_for
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader
from datetime import date
from nlp_analyzer.nlp import analyze_nlp
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from db import get_db
import os
import urllib.request

ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf')
			return redirect(request.url)
            
@app.route('/pdf_info/<path>', methods=['GET'])
def extract_PDFinfo(path):

    if path == "":
        flash('No file selected to extract PDF information')
        redirect(url_for('extract_PDFinfo'))
	
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
            
    metadata = {
        "title": "",
        "author": ""
    }
    metadata["title"] = info.title
    metadata["author"] = info.author
    
    return metadata

@app.route('/text/<path>', methods=['GET'])
def extract_text(path):
    
    if path == "":
        flash('No file selected to extract text')
        redirect(url_for('extract_text'))
	
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(1)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        return text

@app.route('/create/<path>', methods=['GET'])
def create_info(path):
    
    if path == "":
        flash('No file selected')
        redirect(url_for('create_info'))
	
    split_tup = os.path.splitext(path)
    fname = split_tup[0]
    text_content = extract_text(path)
    metadata = extract_PDFinfo(path)
    nlp = analyze_nlp(text_content)
    
    files = {
        "id": "",
        "name": "",
        "upload_date": "",
        "text": "",
        "title": "",
        "author": "", 
        "sentiment_score": "",
        "sentiment_magnitude": "",
        "sentiment": ""
    }

    files["name"] = fname
    files["upload_date"] = str(date.today())
    files["text"] = text_content
    files["title"] = metadata["title"]
    files["author"] = metadata["author"]
    files["sentiment_score"] = nlp["sentiment_score"]
    files["sentiment_magnitude"] = nlp["sentiment_magnitude"]
    files["sentiment"] = nlp["sentiment"]

    return files 
    
@app.route("/add/<path>", methods=["POST", "GET"])
def add_file(path):

    files = create_info(path)
    
    db = get_db()

    file_name = files["name"]
    upload_date = files["upload_date"]
    text = files["text"] 
    title = files["title"]
    author = files["author"] 
    sentiment_score = files["sentiment_score"]
    sentiment_magnitude= files["sentiment_magnitude"] 
    sentiment = files["sentiment"]
    
    db.execute(
        'INSERT INTO Files (file_name, upload_date, text, title, author, sentiment_score, sentiment_magnitude, sentiment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (file_name, upload_date, text, title, author, sentiment_score, sentiment_magnitude, sentiment,)
    )
    db.commit()
    flash('Successfully added to DB', category='alert alert-info')
    return redirect(url_for('upload_form'))

if __name__ == "__main__":
    app.run(debug=True)