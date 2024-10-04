# Python

import json

# This file will test JSON data and dictionaries.
test_dictionary = {
    'Name' : 'Uncle Bob',
    'Age' : 57,
    'Home': 'Rockport',
    'Hobby1': 'Rock Climbing'
}
print(test_dictionary)
print(test_dictionary['Name'])
json_string = json.dumps(test_dictionary)
with open('JSONExampleTake3.json', 'w') as file_handle:
    file_handle.write(json_string)

with open('JSONExampleTake3.json', 'r') as file_handle:
    json_string = file_handle.read()
    print(json_string)
    json_dictionary = json.loads(json_string)
    print(json_dictionary['Name'])
