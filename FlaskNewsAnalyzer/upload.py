import os
from flask import(
   Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.utils import secure_filename

bp = Blueprint('upload', __name__, url_prefix='/upload')

# app.secret_key = "secret key"
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

UPLOAD_DIR="/uploads"

ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def upload_form():
    return render_template('upload.html')

@bp.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Invalid file type')
            return redirect(request.url)
