from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)

bp = Blueprint('newsfeed_ingest', __name__, url_prefix='/newsfeed_ingest')

@bp.route("/", methods=('GET', 'POST'))
def search_title():
    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        title = request.form['title']
        
        if name == "" and title == "":
            return redirect(url_for('bp.newsfeed_ingest'))
        elif name != "" and title == "":
            file_info = db.execute('select * from file where name = "%s"'%(name))
        elif title != "" and name == "":
            file_info = db.execute('select * from file where title = ?', (title,))
        elif name != "" and title != "":
            file_info = db.execute('select * from file where name = ? and title = ?',(name, title,))
        else: 
            return render_template('newsfeed_ingest.html', name=name, title=title, file_info=file_info)
    file_info = db.execute('SELECT * from file')
    return render_template('newsfeed_ingest.html', file_info=file_info)

## def search_nlp():
    

