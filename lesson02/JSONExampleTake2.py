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
json_dictionary = json.loads(json_string)
print(json_string)

print(type(test_dictionary))
print(type(json_string))
print(type(json_dictionary))
print(json_dictionary['Name'])

with open('JSONExampleTake2.json', 'w') as file_handle:
    #file_handle.write(test_dictionary)
    #file_handle.write(json_data)
    file_handle.write(json_string)


with open('JSONExampleTake2.json', 'r') as file_handle:
    json_string = file_handle.read()
    print(json_string)

#rint(json_string['Name'])

json_dictionary = json.loads(json_string)
print(json_dictionary['Name'])
