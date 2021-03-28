from flask import Flask, flash, request, redirect, render_template, json, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app import app
from db import get_db
import logging 

@app.route("/")
def index():
    return render_template('upload_index.html')
    
@app.route("/<keyword>", methods=["GET"])
def search_id(keyword):
    db = get_db()
    
    files = db.execute(
        'SELECT * FROM Files WHERE file_id = ? ORDER BY file_id or file_name = ? ORDER BY file_id or upload_date = ? ORDER BY file_id or text = ? ORDER BY file_id or title = ? ORDER BY file_id or author = ? ORDER BY file_id or sentiment = ? ORDER BY file_id', 
        (keyword,keyword, keyword, keyword, keyword, keyword, keyword)
    ).fetchall()
    #result = db.execute('SELECT * FROM Files WHERE file_name = ?', (keyword,)).fetchall()
    #result = db.execute('SELECT * FROM Files WHERE upload_date = ?', (keyword,)).fetchall()
    #result = db.execute('SELECT * FROM Files WHERE text = ?', (keyword,)).fetchall()
    #result = db.execute('SELECT * FROM Files WHERE title = ?', (keyword,)).fetchall()
    #result = db.execute('SELECT * FROM Files WHERE author = ?', (keyword,)).fetchall()
    #result = db.execute('SELECT * FROM Files WHERE sentiment = ?', (keyword,)).fetchall()
    if files is None:
        return redirect('error_handler')
    else:
        #return jsonify(files) 
        return render_template('upload_index.html', files=files)
    
def error_handler():
    return "Invalid input"

if __name__ == '__main__':
    app.run(debug=True)