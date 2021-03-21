import os
import PyPDF2
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session, current_app
)
from werkzeug import secure_filename

bp = Blueprint('pdf_convert', __name__, url_prefix='/pdf')

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['pdf'])
## app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
## app.config['SECRET_KEY'] = os.urandom(24)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@bp.route('/')
def index():
    return render_template('pdf.html')

@bp.route('/show_pdf', methods=['GET', 'POST'])
def show_pdf():
    if request.method == 'POST':
        send_data = request.files['send_data']
        if send_data and allowed_file(send_data.filename):
            filename = secure_filename(send_data.filename)
            send_data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdf_file_obj = open('uploads/' + filename, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            page_obj = pdf_reader.getPage(0)
            result = page_obj.extractText()

            return render_template('pdf.html', result=result)

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


