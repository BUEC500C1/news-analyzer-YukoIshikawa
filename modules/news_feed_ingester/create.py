import json

def create():
  file_path = "./sample.json"
  json_data = {}
  with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    
    json_data['posts'].append({
    "title": "How to parse JSON in android",
    "url": "https://codechacha.com/ko/how-to-parse-json-in-android/",
    "draft": "true"
    })
    with open(file_path, 'w') as outfile:
    json.dump(json_data, outfile, indent=4)
    return "fail"

    
