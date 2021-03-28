from flask import Flask, request, json, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

files = {
    '1': 'Thanksgiving Advice for BU Students: Stick Around, Have a Safe Friendsgiving',
    '2': 'ENG’s David Bishop Tapped as Member of National Academy of Engineering'
}

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to my Resst API!'})

@app.route('/files', methods=['GET'])
def list_all_files():
    json = {
        'message': files
    }
    return jsonify(json)
    
@app.route('/files/<int:fileid>', methods=['GET'])
def show_file(fileid):
    fileid = str(fileid)
    json = {
        'message': files[fileid]
    }
    return jsonify(json)
    
@app.route('/files/<int:fileid>', methods=['DELETE'])
def delete_file(fileid):
    fileid = str(fileid)
    if fileid in files:
        del files[fileid]
        msg = 'File {} deleted'.format(fileid)
    else:
        msg = '{0} is not in files.'.format(fileid)
    json = {
        'message': msg
    }
    return jsonify(json)
    
@app.route('/files', methods=['POST'])
def create_file():
    filed = str(int(max(files.keys())) + 1)
    posted = request.get_json()
    if 'file' in posted:
        files[fileid] = posted['file']
        msg = 'New sile created'
    else:
        msg = 'No sile created'
    json = {
        'message': msg
    }
    return jsonify(json)
    
@app.route('/files/<int:fileid>', methods=['PUT'])
def update_file(fileid):
    fileid = str(fileid)
    posted = request.get_json()
    if 'file' in posted and fileid in files:
        files[fileid] = posted['file']
        msg = 'File {} updated'.format(fileid)
    else:
        msg = 'No file updated'
    json = {
        'message': msg
    }
    return jsonify(json)

if __name__ == "__main__":
    ## app.run(debug=True)
    app.run(host = '0.0.0.0', port = 443)