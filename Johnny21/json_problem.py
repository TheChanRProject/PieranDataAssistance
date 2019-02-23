import json

file = open('sample.json')
file_string = file.read()
json_data = json.loads(file_string)
