import json


data = {
    'name' : 'Jonh Doe',
    'age' : 88,
    'ocupation' : 'Software Engineer'


}

with open("buf.txt", "w",) as f:
    json.dump(data, f, indent=4)