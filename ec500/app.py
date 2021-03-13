from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Text

engine = create_engine('sqlite:///texts-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/texts')
def showTexts():
    texts = session.query(Text).all()
    return render_template('texts.html', texts=texts)


@app.route('/texts/new/', methods=['GET', 'POST'])
def newText():
    if request.method == 'POST':
        newText = Text(title=request.form['name'],
                       author=request.form['author'],
                       genre=request.form['genre'])
        session.add(newText)
        session.commit()
        return redirect(url_for('showTexts'))
    else:
        return render_template('newText.html')


@app.route("/texts/<int:text_id>/edit/", methods=['GET', 'POST'])
def editText(text_id):
    editedText = session.query(Text).filter_by(id=text_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedText.title = request.form['name']
            return redirect(url_for('showTexts'))
    else:
        return render_template('editText.html', Text=editedText)


@app.route('/texts/<int:text_id>/delete/', methods=['GET', 'POST'])
def deleteText(text_id):
    textToDelete = session.query(Text).filter_by(id=text_id).one()
    if request.method == 'POST':
        session.delete(textToDelete)
        session.commit()
        return redirect(url_for('showTexts', text_id=text_id))
    else:
        return render_template('deleteText.html', Text=textToDelete)



from flask import jsonify


def get_texts():
    texts = session.query(Text).all()
    return jsonify(texts=[b.serialize for b in texts])


def get_text(text_id):
    texts = session.query(Text).filter_by(id=text_id).one()
    return jsonify(texts=texts.serialize)


def makeANewText(title, author, genre):
    addedtext = Text(title=title, author=author, genre=genre)
    session.add(addedtext)
    session.commit()
    return jsonify(Text=addedtext.serialize)


def updateText(id, title, author, genre):
    updatedText = session.query(Text).filter_by(id=id).one()
    if not title:
        updatedText.title = title
    if not author:
        updatedText.author = author
    if not genre:
        updatedText.genre = genre
    session.add(updatedText)
    session.commit()
    return 'Updated a Text with id %s' % id


def deleteAText(id):
    textToDelete = session.query(Text).filter_by(id=id).one()
    session.delete(textToDelete)
    session.commit()
    return 'Removed Text with id %s' % id


@app.route('/')
@app.route('/textsApi', methods=['GET', 'POST'])
def textsFunction():
    if request.method == 'GET':
        return get_texts()
    elif request.method == 'POST':
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        genre = request.args.get('genre', '')
        return makeANewText(title, author, genre)


@app.route('/textsApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def textFunctionId(id):
    if request.method == 'GET':
        return get_text(id)

    elif request.method == 'PUT':
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        genre = request.args.get('genre', '')
        return updateText(id, title, author, genre)

    elif request.method == 'DELETE':
        return deleteAText(id)


if __name__ == '__main__':
    app.run(debug=True)
    app.debug = True
    app.run(host='0.0.0.0', port=4996)