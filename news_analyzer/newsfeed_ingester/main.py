from flask import Flask, abort, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
 
article = [
        "File_Name" : (file_name), type=str)
        "File_URI" : (file_uri, type=str) 
        "File_Type" : (file_type, type=str) 
        "Metadata" : (metadata, type=object) {
            "Author" : (author, type=str)
            "Published_At" : (published_at, type=str) 
            "Source" : (source, type=object) {
                "Source" : (source, type=str) 
                "Search_param" : (search_param, type=list) 
                "Filters" : (filters, type=list) 
            }
          ]

class User(Resource):
    def get(self):
        id = request.args.get('id')
        result = [n for n in users if n["id"] == id]

        if len(result) >= 1: 
            return result[0]
        else:
            abort(404)

    def post(self):
        users.append(request.json)

        return '', 204

    def put(self):
        user = request.json
        lst = [val for val in users if val["id"] == text["id"]]
        
        if len(lst) >= 1: 
            lst[0]["name"] = user["name"]
            lst[0]["age"] = user["age"]
        else:
            abort(404)
            
        return '', 204

    def delete(self):
        id = request.args.get('id')
        lst = [i for i, val in enumerate(users) if val["id"] == id]
        for index in lst:
            del users[index]

        if len(lst) >= 1: 
            return '', 204
        else:
            abort(404)

api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(debug=True)
